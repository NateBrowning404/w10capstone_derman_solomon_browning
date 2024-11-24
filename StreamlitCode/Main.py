import streamlit as st

# Set up for the page navigation -----
st.set_page_config(initial_sidebar_state="expanded") # Keeps the sidebar open for when you first open the page

# Navigation setup
pages = {
    "Main": [
        st.Page("pages/Home.py", title="Home",icon=":material/home:"),
        st.Page("pages/Background.py", title="Background",icon=":material/psychology:"),
        st.Page("pages/Contact.py", title="Contact", icon=":material/mail:"),
        st.Page("pages/About_Us.py", title="About The Team", icon=":material/group:"),
        st.Page("pages/Demo.py", title="Tool Demo", icon=":material/album:"),
        st.Page("pages/Privacy_Policy.py", title="Privacy Policy", icon=":material/security:"),
    ]
}

# Navigation function call
pg = st.navigation(pages,position ="sidebar")

# Sidebar message
st.sidebar.text("Property of Marine Microplastics")

# Run the pages
pg.run() 



