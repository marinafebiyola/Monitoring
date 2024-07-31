import streamlit as st
import requests
import time

st.title("Monitoring System")

# Fungsi untuk mendapatkan data acak dari backend
def get_random_data():
    try:
        response = requests.get("https://light-news-fry.loca.lt/random-data")
        data = response.json()
        return data['data']
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Menampilkan data acak secara terus-menerus
st.write("Menampilkan data acak secara terus-menerus...")

while True:
    # Mendapatkan data acak
    data = get_random_data()
    
    # Menampilkan data acak di frontend
    if data is not None:
        st.write(f"Data Acak: {data}")


    # Refresh halaman
    st.experimental_rerun()
