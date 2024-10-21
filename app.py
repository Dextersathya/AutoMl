from operator import index
import streamlit as st
import plotly.express as px
from ydata_profiling import ProfileReport
import pandas as pd
from streamlit_pandas_profiling import st_profile_report

import os

# Load dataset if exists
if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

# Sidebar navigation
with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoNickML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

# Upload section
if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

# Profiling section
if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    profile_df = ProfileReport(df)
    st_profile_report(profile_df)

# Modelling section
if choice == "Modelling":
    pass

# Download section
if choice == "Download": 
    with open('best_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="best_model.pkl")
