import streamlit as st
import requests
import time

st.title("Monitoring")

data_placeholder = st.empty()

while True:
    try:
        response = requests.get("https://tangy-pears-cover.loca.lt/random-data", timeout=5)
        response.raise_for_status()
        data = response.json()
        st.write(f"Data Acak: {data['data']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request gagal: {e}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
    
    time.sleep(3)  # Interval waktu yang lebih stabil untuk pengiriman data
