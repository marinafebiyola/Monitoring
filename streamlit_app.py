import streamlit as st
import socketio

# Koneksi ke server backend Flask dengan WebSocket
sio = socketio.Client()

# Callback untuk menerima data dari server
@sio.event
def data_response(data):
    st.text(f"Data Acak: {data['data']}")

def main():
    st.title("Monitoring Data Real-Time")

    # Alamat URL server backend Flask yang dijalankan
    # Ganti 'http://127.0.0.1:5000' sesuai dengan alamat yang sesuai dengan server Flask Anda
    server_url = 'http://127.0.0.1:5000'
    
    with st.spinner(f'Connecting to WebSocket at {server_url}...'):
        sio.connect(server_url)

    # Minta data dari server saat terhubung
    sio.emit('request_data')

    st.text("Menunggu data real-time...")

if __name__ == '__main__':
    main()
