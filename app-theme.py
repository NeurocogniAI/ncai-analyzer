import streamlit as st

# Set initial theme (you can change this)
st.set_page_config(layout="wide", page_title="Dark/Light Mode App")

# Toggle button for theme switching
theme_toggle = st.button("Toggle Theme")

# Function to set the theme dynamically
def set_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"  # Default to dark theme

    if theme_toggle:
        if st.session_state.theme == "light":
            st.session_state.theme = "dark"
        else:
            st.session_state.theme = "light"

    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #010D2D;  # Dark background color
            }
            
            .stApp * {
                color: #ADD8E6;  # Light blue text color
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #FFFFFF;  # Light background color
                color: #000000;  # Dark text color
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Call the function to set the initial theme
set_theme()

# Example content (replace with your actual app content)
st.title("Welcome to the App")
st.write("This is a simple example of a Streamlit app with dark/light mode.")

# You can add more content here...