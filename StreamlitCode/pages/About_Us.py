import streamlit as st

st.title("Meet The Team")
st.write("Meet the members of the Marine Microplastics team below!")

col1, col2, col3 = st.columns(3,gap="medium")

with col1:
    st.header("Daniel Solomon")
    st.image("https://ca.slack-edge.com/T0WA5NWKG-U04AJH1A6QN-b61b1af643be-512")
    st.write("Machine Learning Lead")

with col2:
    st.header("Kayla Derman")
    st.image("https://ca.slack-edge.com/T0WA5NWKG-U05KTKNHY0N-58edbf1ab62a-512")
    st.write("Data Engineering Lead")

with col3:
    st.header("Nathaniel Browning")
    st.image("https://ca.slack-edge.com/T0WA5NWKG-U026VEUL1J7-b3bcdfe4ad20-512")
    st.write("Front-End Lead")
