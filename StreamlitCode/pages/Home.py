import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import random
import geopandas as gpd
import pickle
import xgboost


st.title("Marine Microplastics")
st.write("Welcome to the tool!\nBelow you will find two inputs that will drive the output of the model.")
         
df = pd.read_csv('agg_data.csv')
fish = set(list(df[df['Commercial status']=='highly commercial']['Common name']))

st.subheader("Input 1: Fishtype")
st.write("Enter the species of fish you are inquiring about:")

fishtype = st.selectbox(
    'What type of fish are you looking into?',
    fish,
    )

st.subheader("Input 2: Fish Location")
st.write("If possible, click on the region that the fish in question would have been native to or captured at:")

# Load the province data
gdf = gpd.read_file('Savoca/Longhurst_world_v4_2010.shp')

if gdf is not None:
    # Convert the CRS to WGS84 if it's not already
    if gdf.crs != "EPSG:4326":
        gdf = gdf.to_crs("EPSG:4326")
    
    # Create the base map centered on a global view
    m = folium.Map(location=[30, 0], zoom_start=2)
    
    # Style function for the GeoJSON layer
    def style_function(feature):
        return {
            'fillColor': '#3388ff',
            'fillOpacity': 0.2,
            'color': '#1f4780',
            'weight': 1,
        }

    # Highlight function for mouseover
    def highlight_function(feature):
        return {
            'fillColor': '#3388ff',
            'fillOpacity': 0.6,
            'color': '#1f4780',
            'weight': 3,
        }
    
    # Add GeoJSON layer with interactive features
    folium.GeoJson(
        gdf,
        name='Marine Provinces',
        style_function=style_function,
        highlight_function=highlight_function,
        popup=folium.GeoJsonPopup(
            fields=['ProvCode', 'ProvDescr'],
            aliases=['Province Code:', 'Description:'],
            style="background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"
        )
    ).add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Display the map
    folium_static(m)
    
    # Add selection functionality in sidebar
    st.sidebar.header("Province Selection")
    
    selected_province = st.sidebar.selectbox(
        "Select a Marine Province:",
        gdf['ProvDescr'].sort_values().unique()
    )
    
    # Display selected province information
    if selected_province:
        st.sidebar.subheader("Province Information")
        province_data = gdf[gdf['ProvDescr'] == selected_province].iloc[0]
        st.sidebar.text(f"Province Code: {province_data['ProvCode']}")
        st.sidebar.text(f"Description: {province_data['ProvDescr']}")
        
        # Add a button to zoom to selected province
        if st.sidebar.button("Zoom to Selected Province"):
            # Get the bounds of the selected province
            bounds = gdf[gdf['ProvDescr'] == selected_province].geometry.total_bounds
            # Update map center and zoom
            m.fit_bounds([[bounds[1], bounds[0]], [bounds[3], bounds[2]]])
            # Redisplay the map
            folium_static(m)

# Button to Run Model

#st.write("Click this button to receive a result")

# load saved model from pickle file
with open('xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

if st.button('Run Model'):

    prediction = random.randint(0,2)

    st.write(prediction)

    col1, col2 = st.columns(2)

    with col1:
        if prediction == 2:
            st.markdown(f'<div style="background-color: #BB4430; padding: 10px; border-radius: 5px; color: #FFFFFF;">High Risk</div>', unsafe_allow_html=True)
        elif prediction == 1:
            st.markdown(f'<div style="background-color: #F8C630; padding: 10px; border-radius: 5px; color: #FFFFFF;">Medium Risk</div>', unsafe_allow_html=True)
        elif prediction == 0:
            st.markdown(f'<div style="background-color: #568259; padding: 10px; border-radius: 5px; color: #FFFFFF;">Low Risk</div>', unsafe_allow_html=True)

    with col2:
        if prediction == 2:
            st.write("The fish you are inquiring about could be at high risk for microplastic contamination. This rating is indicative of a predction that their is an average consumption of over 10 microplastics for this fish.")
        elif prediction == 1:
            st.write("The fish you are inquiring about could be at medium risk for microplastic contamination. This rating is indicative of a predction that their is an average consumption between 3 and 10 microplastics for this fish.")
        elif prediction == 0:
            st.write("The fish you are inquiring about could be at medium risk for microplastic contamination. This rating is indicative of a predction that their is an average consumption of less than 3 microplastics for this fish.")

st.write(selected_province)
