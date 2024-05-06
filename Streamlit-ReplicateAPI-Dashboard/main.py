import streamlit as st
from dotenv import load_dotenv

from generate_image import generate_image
from image_to_prompt import image_to_prompt
from remove_background import remove_background

load_dotenv()

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Replicate API Dashboard")

# Sidebar
st.sidebar.title("AI Tools")

# State variables
current_page = st.sidebar.radio("Tools", ["Generate Image", "Image to Prompt", "Remove Background"], key="page_selector",
                                label_visibility="hidden")

# Generate Image
if current_page == "Generate Image":
    generate_image()

# Image to Prompt
if current_page == "Image to Prompt":
    image_to_prompt()

# Remove Background
if current_page == "Remove Background":
    remove_background()
