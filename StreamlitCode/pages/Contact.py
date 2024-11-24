import streamlit as st

st.title("Contact Us")
st.write("Like what you see? Have any questions for the group? \n Feel free to send us a note through the form below!")

contact_form = """
<form action="https://formsubmit.co/njbrowni@berkeley.edu" method="POST">
     <input type="hidden" name="_captcha" value="false"
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name= "message" placeholder="Type your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


local_css("styling/form_style.css")