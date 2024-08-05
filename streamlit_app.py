import streamlit as st
import requests
import time

st.title("Monitoring")

data_placeholder = st.empty()

while True:
    response = requests.get("https://d334-182-2-5-35.ngrok-free.app/random-data")
    data = response.json()  # This line is causing the JSONDecodeError
    data_placeholder.write(f"Data Acak: {data['data']}")
    time.sleep(5)  # Adjust the sleep time as needed to control the update frequency
