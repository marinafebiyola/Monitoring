import streamlit as st
import requests
import time

st.title("Monitoring system")

data_placeholder = st.empty()

while True:
    response = requests.get("https://ce94-103-20-185-106.ngrok-free.app/random-data")
    data = response.json()  # This line is causing the JSONDecodeError
    data_placeholder.write(f"Data Acak: {data['data']}")
   
