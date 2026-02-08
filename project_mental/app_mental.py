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

    add_bg_from_local("../mental_health/xray.jpg")
    st.markdown(
        """
        <p style='color: #FFFFFF; font-size: 16px;'>
            Mental health is a crucial component of overall well-being, yet it is often overlooked or misunderstood.
            Early detection and timely intervention can significantly improve outcomes for individuals experiencing mental health challenges.
            Mental health issues such as anxiety, depression, and burnout are becoming increasingly prevalent in today's fast-paced and high-stress environments. Despite growing awareness, many individuals continue to suffer silently due to stigma, lack of access to care, or unawareness of their mental health condition. In this context, technology—especially artificial intelligence and machine learning—can play a transformative role in early detection and awareness.This project presents a Mental Health Prediction System developed using machine learning techniques to help identify individuals who may be at risk of mental health challenges. The application gathers input data based on various personal, professional, and behavioral factors (such as age, gender, workplace environment, support systems, etc.) and predicts the likelihood of mental health issues using a trained ML model.
            emotional well-being using scientifically validated tools and methods. Mental health conditions such as depression, anxiety, bipolar disorder, and stress-related disorders often go undiagnosed due to stigma or lack of awareness. By implementing reliable mental health screening—whether through questionnaires, clinical interviews, or AI-powered prediction tools—individuals can better understand their mental state and seek timely professional support. These tests not only help in early detection but also guide tailored interventions and treatment plans, ultimately improving the individual’s quality of life and reducing long-term healthcare burdens. As mental health awareness continues to grow globally, testing is becoming a critical first step toward fostering a healthier, more resilient society.


        </p>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Go to", ["Home", "check"])

    # Based on selection, show different content
    if option == "H":
        st.write("Welcome to the Home Page!")
    elif option == "check":
        st.switch_page("project_mental/pages/checking.py")
main()

