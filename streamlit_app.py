import streamlit as st
import requests
import time

st.title("Monitoring")

data_placeholder = st.empty()

while True:
    response = requests.get("https://86dc-103-20-185-106.ngrok-free.app /random-data")
    data = response.json()  # This line is causing the JSONDecodeError
    data_placeholder.write(f"Data Acak: {data['data']}")
    time.sleep(5)  # Adjust the sleep time as needed to control the update frequency
