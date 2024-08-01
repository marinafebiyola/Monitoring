import streamlit as st
import requests
import time

st.title("Monitoring")

data_placeholder = st.empty()

while True:
    try:
        response = requests.get("https://odd-seas-listen.loca.lt/random-data", timeout=5)
        response.raise_for_status()
        data = response.json()
        data_placeholder.text(f"Data Acak: {data['data']}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
    
    time.sleep(3)  # Interval waktu yang lebih stabil untuk pengiriman data
