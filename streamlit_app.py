import streamlit as st
import requests

st.title("Monitoring system")

if st.button("Dapatkan Data Acak"):
    response = requests.get("https://light-news-fry.loca.lt/random-data")
    data = response.json()
    st.write(f"Data Acak: {data['data']}")
