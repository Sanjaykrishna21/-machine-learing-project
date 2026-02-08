import os.path
from fileinput import filename

import streamlit as st
import pickle
from PIL import Image
import base64
def main():
    st.markdown("<h1 style='text-align: center; color: #FF4500;'>MENTAL HEALTH</h1>", unsafe_allow_html=True)

    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
                <style>
                .stApp {{
                    background-image: url("data:image/jpg;base64,{encoded}");
                    background-attachment: fixed;
                    background-size: cover;
                }}
                </style>
                """,
            unsafe_allow_html=True
        )

    add_bg_from_local("xray.jpg")
main()