# import os, pathlib, streamlit, google.generativeai
import os
import pathlib
import streamlit as st
import google.generativeai as genai

# setting up the page configuration
st.set_page_config(
    page_title="Life Medical AI Assistant", page_icon=":robot", layout="centered", initial_sidebar_state="expanded"
)

logo_path = pathlib.Path("./logo.jpg")
# create the image in the sidebar
# st.sidebar.image(logo_path, use_column_width=True)

st.title("Life Medical AI Assistant 🤖")

st.subheader("Welcome to the new revolutionizing solution to Life🏥")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

submit = st.button("Generate Report 📄")

if submit:
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write("")
        st.write("Classifying the image...")

        # Load the model
        model = genai.load_model