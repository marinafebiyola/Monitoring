import streamlit as st
import requests
import time

st.title("Monitoring system")

data_placeholder = st.empty()

while True:
    response = requests.get("http://localhost:5000/random-data")
    data = response.json()  # This line is causing the JSONDecodeError
    data_placeholder.write(f"Data Acak: {data['data']}")
    time.sleep(5)  # Adjust the sleep time as needed to control the update frequency
