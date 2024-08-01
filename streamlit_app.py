import streamlit as st
import requests
import time

st.title("Monitoring")

data_placeholder = st.empty()

while True:
    try:
        response = requests.get("https://late-berries-cough.loca.lt/random-data", timeout=5)
        response.raise_for_status()
        data = response.json()
        data_placeholder.text(f"Data Acak: {data['data']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request gagal: {e}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
    
    time.sleep(5)  # Tunggu sebelum mencoba lagi
