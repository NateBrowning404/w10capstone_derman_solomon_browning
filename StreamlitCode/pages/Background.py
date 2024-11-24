import streamlit as st

st.title("Background")



st.subheader("Our Mission")
st.write("Our mission is to provide consumers with the knowledge and capabilities to predict their potential exposure to microplastics via seafood. Our goal is to place the power of risk minimization in the hands of consumers through the power of analytics. ")


st.subheader("Data Sources")
with st.expander("**CYGNSS Dataset**"):
    st.write('''The CYGNSSS data set displays the concentration of microplastics 
             across all oceans using satellite imagery. This data is updated daily and extends
             back as far as 2018.
             ''')
    st.image("https://eoimages.gsfc.nasa.gov/images/imagerecords/149000/149163/microplastics_cygnss_2018098.jpg")


with st.expander("**Savoca Dataset**"):
    st.write('''The Savoca Dataset contains a series of real-life studies accumulated
             over several years that measures microplastic accumulation in the stomachs of 
             fish. This study is used to help train our predictive model.
             ''')
    st.image("https://imgs.search.brave.com/RkuJWtLVB2s7qy5TdlYyyI3T9ELlh7A6Orhy5y4mGSg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTM0/OTg3MzY3L3Bob3Rv/L3NhbG1vbi5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9WnZD/dGlFRlptUUgyQ1NM/Qm9rRnhydWEtUlg5/MGZhc1dpVzB6QWtk/ZTBDRT0")

st.subheader("How does the Tool Work?")
st.write("The Marine Microplastics tool requires two inputs for full operation")
st.write("**Input 1:** The first input will ask for the common name of the species of fish you are inquiring about.")
st.write("**Input 2:** The second input (optional) allows for you to click on the region that you believe your fish is native to or was captured at.")
st.write('''**Model:** Your inputs are run through an XGBoost model that trains on our listed data sets. 
         The XGBoost Model will output a prediction of microplastic accumulation in the fish you are referencing.
         The output will be a value that will fit into one of three set thresholds; Red, Yellow, or Green.
         ''')

st.subheader("Output Thresholds")