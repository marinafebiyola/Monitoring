import streamlit as st
import requests

st.title("Monitoring System")

def get_random_data():
    try:
        response = requests.get("http://127.0.0.1:5000/random-data")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Server returned status code {response.status_code}")
            return None
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

st.write("Menampilkan data acak secara terus-menerus...")

while True:
    data = get_random_data()
    if data:
        st.write(f"Data Acak: {data.get('data')}")
    time.sleep(5)
