# -*- coding: utf-8 -*-
"""Streamlit_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CpQrMBwgWUO8YMjNh9JVbqJCZ1NOxe40
"""

!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile requiredment.txt
# alembic==1.8.1
# altair==4.2.0
# asttokens==2.0.8
# attrs==22.1.0
# backcall==0.2.0
# blinker==1.5
# blis==0.7.9
# Boruta==0.3
# cachetools==5.2.0
# catalogue==1.0.2
# certifi==2022.9.24
# charset-normalizer==2.1.1
# click==8.1.3
# cloudpickle==2.2.0
# colorama==0.4.6
# colorlover==0.3.0
# commonmark==0.9.1
# cufflinks==0.17.3
# cycler==0.11.0
# cymem==2.0.7
# databricks-cli==0.17.3
# debugpy==1.6.3
# decorator==5.1.1
# docker==6.0.0
# entrypoints==0.4
# executing==1.1.1
# Flask==2.2.2
# fonttools==4.38.0
# funcy==1.17
# future==0.18.2
# gensim==3.8.3
# gitdb==4.0.9
# GitPython==3.1.29
# greenlet==1.1.3.post0
# htmlmin==0.1.12
# idna==3.4
# ImageHash==4.3.1
# imbalanced-learn==0.7.0
# importlib-metadata==5.0.0
# ipykernel==6.16.2
# ipython==8.5.0
# ipywidgets==8.0.2
# itsdangerous==2.1.2
# jedi==0.18.1
# Jinja2==3.1.2
# joblib==1.2.0
# jsonschema==4.16.0
# jupyter_client==7.4.4
# jupyter_core==4.11.2
# jupyterlab-widgets==3.0.3
# kiwisolver==1.4.4
# kmodes==0.12.2
# lightgbm==3.3.3
# llvmlite==0.37.0
# Mako==1.2.3
# MarkupSafe==2.1.1
# matplotlib==3.5.3
# matplotlib-inline==0.1.6
# missingno==0.5.1
# mlflow==1.30.0
# mlxtend==0.19.0
# multimethod==1.9
# murmurhash==1.0.9
# nest-asyncio==1.5.6
# networkx==2.8.7
# nltk==3.7
# numba==0.54.1
# numexpr==2.8.3
# numpy==1.20.3
# oauthlib==3.2.2
# packaging==21.3
# pandas==1.5.1
# pandas-profiling==3.4.0
# parso==0.8.3
# patsy==0.5.3
# phik==0.12.2
# pickleshare==0.7.5
# Pillow==9.2.0
# plac==1.1.3
# plotly==5.10.0
# preshed==3.0.8
# prometheus-client==0.15.0
# prometheus-flask-exporter==0.20.3
# prompt-toolkit==3.0.31
# protobuf==3.20.3
# psutil==5.9.3
# pure-eval==0.2.2
# pyarrow==9.0.0
# pycaret==2.3.10
# pydantic==1.10.2
# pydeck==0.8.0b4
# Pygments==2.13.0
# PyJWT==2.6.0
# pyLDAvis==3.3.1
# Pympler==1.0.1
# pynndescent==0.5.7
# pyod==1.0.6
# pyparsing==3.0.9
# pyrsistent==0.18.1
# python-dateutil==2.8.2
# pytz==2022.5
# pytz-deprecation-shim==0.1.0.post0
# PyWavelets==1.4.1
# pywin32==304
# PyYAML==5.4.1
# pyzmq==24.0.1
# querystring-parser==1.2.4
# regex==2022.9.13
# requests==2.28.1
# rich==12.6.0
# scikit-learn==0.23.2
# scikit-plot==0.3.7
# scipy==1.5.4
# seaborn==0.12.1
# semver==2.13.0
# six==1.16.0
# sklearn==0.0
# smart-open==6.2.0
# smmap==5.0.0
# spacy==2.3.8
# SQLAlchemy==1.4.42
# sqlparse==0.4.3
# srsly==1.0.6
# stack-data==0.5.1
# statsmodels==0.13.2
# streamlit==1.13.0
# streamlit-pandas-profiling==0.1.3
# tabulate==0.9.0
# tangled-up-in-unicode==0.2.0
# tenacity==8.1.0
# textblob==0.17.1
# thinc==7.4.6
# threadpoolctl==3.1.0
# toml==0.10.2
# toolz==0.12.0
# tornado==6.2
# tqdm==4.64.1
# traitlets==5.5.0
# typing_extensions==4.4.0
# tzdata==2022.5
# tzlocal==4.2
# umap-learn==0.5.3
# urllib3==1.26.12
# validators==0.20.0
# visions==0.7.5
# waitress==2.1.2
# wasabi==0.10.1
# watchdog==2.1.9
# wcwidth==0.2.5
# websocket-client==1.4.1
# Werkzeug==2.2.2
# widgetsnbextension==4.0.3
# wordcloud==1.8.2.2
# yellowbrick==1.2.1
# zipp==3.10.0

!pip install -r requiredment.txt

# Commented out IPython magic to ensure Python compatibility.
# # Create the Streamlit app script
# %%writefile app.py
# from operator import index
# import streamlit as st
# import plotly.express as px
# from pycaret.regression import setup, compare_models, pull, save_model, load_model
# import pandas_profiling
# import pandas as pd
# from streamlit_pandas_profiling import st_profile_report
# import os
# 
# if os.path.exists('./dataset.csv'):
#     df = pd.read_csv('dataset.csv', index_col=None)
# 
# with st.sidebar:
#     st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
#     st.title("AutoNickML")
#     choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
#     st.info("This project application helps you build and explore your data.")
# 
# if choice == "Upload":
#     st.title("Upload Your Dataset")
#     file = st.file_uploader("Upload Your Dataset")
#     if file:
#         df = pd.read_csv(file, index_col=None)
#         df.to_csv('dataset.csv', index=None)
#         st.dataframe(df)
# 
# if choice == "Profiling":
#     st.title("Exploratory Data Analysis")
#     profile_df = df.profile_report()
#     st_profile_report(profile_df)
# 
# if choice == "Modelling":
#     chosen_target = st.selectbox('Choose the Target Column', df.columns)
#     if st.button('Run Modelling'):
#         # Separate features and target
#         X = df.drop(columns=[chosen_target])
#         y = df[chosen_target]
# 
#         # Display message to indicate training has started
#         st.write("Training the model with AutoKeras...")
# 
#         # Initialize the AutoKeras model
#         automodel = ak.StructuredDataClassifier(max_trials=10)  # For classification problems
#         # For regression use: automodel = ak.StructuredDataRegressor(max_trials=10)
# 
#         # Train the model
#         automodel.fit(X, y, epochs=10)
# 
#         # Display model summary
#         st.write("Model training completed.")
# 
#         # Evaluate and show the best model
#         best_model = automodel.export_model()
#         st.write("Best Model:", best_model.summary())
# 
#         # Save the best model
#         best_model.save('best_model')
# 
#         st.write("Best model saved as 'best_model_autokeras'.")
# 
# if choice == "Download":
#     with open('best_model.pkl', 'rb') as f:
#         st.download_button('Download Model', f, file_name="best_model.pkl")
#

!pip install autokeras

from pyngrok import ngrok

# Launch the Streamlit app in the background
!streamlit run app.py &

# Create a tunnel using ngrok to access the Streamlit app
public_url = ngrok.connect(port='8501')
public_url

from pyngrok import ngrok

# Get your authtoken from the ngrok dashboard and paste it here
NGROK_AUTHTOKEN = "2nOVoAF1CMYFIjdtaD8ilpGTIFV_69UHxHKDrEd4Lq9R1VJvM"  # Replace with your actual authtoken

# Configure pyngrok with your authtoken
ngrok.set_auth_token(NGROK_AUTHTOKEN)

# Launch the Streamlit app in the background
!streamlit run app.py &

# Create a tunnel using ngrok to access the Streamlit app
# The error was due to missing 'addr' parameter,
# 'port' alone is not enough to define the tunnel.
# Streamlit runs on port 8501 by default,
# so we specify the address explicitly.
public_url = ngrok.connect(addr='8501')

public_url

!pip install pyngrok

from pyngrok import ngrok
import subprocess

# Step 1: Launch the Streamlit app in the background
subprocess.Popen(["streamlit", "run", "ap.py"])

# Step 2: Create a tunnel using ngrok to access the Streamlit app
public_url = ngrok.connect(8501)
print("Streamlit app is available at:", public_url)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ap.py
# import streamlit as st
# st.title("Hello World")

