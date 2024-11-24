import streamlit as st

st.title("Privacy Policy")

# Date
st.write("**Effective Date**: November 2024")


st.subheader("Welcome to Marine Microplastics!")
st.write(
    "Your privacy is important to us. This Privacy Policy explains how we handle the "
    "information you provide when using our application."
)

st.subheader("Information We Collect")
st.write(
    "We do not collect, store, or share any personal data. When you use our application to predict "
    "microplastic contamination risk:\n"
    "- Your inputs (fish species and catch location) are processed temporarily to generate the prediction.\n"
    "- These inputs are not stored or saved after the prediction is made."
)

st.subheader("How We Use Your Information")
st.write(
    "The information you provide is used solely to generate your prediction. "
    "Once the prediction is displayed, your input data is deleted from our system immediately."
)

st.subheader("Third-Party Services")
st.write(
    "We do not share your data with any third-party services. All processing occurs locally within our application."
)

st.subheader("Your Rights")
st.write(
    "Because we do not collect or store any of your data, there is nothing to access, modify, or delete."
)

st.subheader("Updates to This Policy")
st.write(
    "We may update this Privacy Policy from time to time. Any updates will be reflected on this page with an updated 'Effective Date.'"
)

st.subheader("Contact Us")
st.write(
    "If you have any questions about this Privacy Policy, please contact us at njbrowni@berkeley.edu."
)