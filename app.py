# import os, pathlib, streamlit, google.generativeai
import os
import pathlib
import streamlit as st
import google.generativeai as genai

# setting up the page configuration
st.set_page_config(
    page_title="Life Medical AI Assistant", page_icon=":robot", layout="centered", initial_sidebar_state="expanded"
)

# setting up the logo
logo_path = pathlib.Path(__file__).parent
st.image(logo_path, use_column_width=True)