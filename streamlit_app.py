import streamlit as st
import requests
import time

st.title("Monitoring")

while True:
    try:
        response = requests.get("https://smooth-rice-greet.loca.lt/random-data", timeout=5)
        response.raise_for_status()
        data = response.json()
        st.text(f"Data Acak: {data['data']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request gagal: {e}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
    
    time.sleep(1)  # Interval waktu untuk mempercepat pemanggilan data
