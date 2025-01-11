import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('final_model.sav', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Customer Churn Prediction App")

# Input form
st.header("Input Data")

# Features
tenure = st.number_input(
    "Tenure (bulan)", 
    value=15, 
    min_value=0, 
    max_value=61, 
    step=1,  # Step to ensure integer input
    help="Lama pelanggan menggunakan layanan (0-61 bulan)."
)
warehouse_to_home = st.number_input(
    "Jarak Gudang ke Rumah (km)", 
    value=29.0, 
    min_value=5.0, 
    max_value=127.0, 
    help="Jarak antara gudang dan rumah pelanggan dalam kilometer (5-127 km)."
)
num_devices = st.number_input(
    "Jumlah Perangkat Terdaftar", 
    value=4, 
    min_value=1, 
    max_value=6, 
    step=1,  # Step to ensure integer input
    help="Jumlah perangkat yang telah terdaftar dalam akun pelanggan (1-6 perangkat)."
)
prefered_order_cat = st.selectbox(
    "Prefered Order Category", 
    ["Laptop & Accessory", "Mobile Phone", "Fashion", "Others"], 
    help="Kategori pesanan yang paling sering dipilih pelanggan."
)
satisfaction_score = st.slider(
    "Skor Kepuasan (1-5)", 
    min_value=1, 
    max_value=5, 
    value=3, 
    help="Skor kepuasan pelanggan terhadap layanan (1-5)."
)
marital_status = st.selectbox(
    "Marital Status", 
    ["Single", "Married", "Divorced"], 
    help="Status pernikahan pelanggan."
)
num_address = st.number_input(
    "Jumlah Alamat Terdaftar", 
    value=2, 
    min_value=1, 
    max_value=22, 
    step=1,  # Step to ensure integer input
    help="Jumlah alamat yang terdaftar pada akun pelanggan (1-22 alamat)."
)
complain = st.selectbox(
    "Pernah Mengeluh?", 
    [0, 1], 
    format_func=lambda x: "Ya" if x == 1 else "Tidak", 
    help="Apakah pelanggan pernah mengeluh? (0: Tidak, 1: Ya)."
)
days_since_last_order = st.number_input(
    "Hari Sejak Pesanan Terakhir", 
    value=7, 
    min_value=0, 
    max_value=46, 
    step=1,  # Step to ensure integer input
    help="Jumlah hari sejak pelanggan terakhir memesan (0-46 hari)."
)
cashback_amount = st.number_input(
    "Jumlah Cashback (Rp)", 
    value=143.32, 
    min_value=0.0, 
    max_value=324.99, 
    help="Jumlah cashback yang diterima pelanggan dalam Rupiah (0-324.99)."
)

# Create DataFrame with the exact column names used during training
input_data = pd.DataFrame({
    "Tenure": [tenure],
    "WarehouseToHome": [warehouse_to_home],
    "NumberOfDeviceRegistered": [num_devices],
    "PreferedOrderCat": [prefered_order_cat],
    "SatisfactionScore": [satisfaction_score],
    "MaritalStatus": [marital_status],
    "NumberOfAddress": [num_address],
    "Complain": [complain],
    "DaySinceLastOrder": [days_since_last_order],
    "CashbackAmount": [cashback_amount]
})

# Prediction button
if st.button("Predict"):
    # Make prediction directly
    prediction = model.predict(input_data)[0]
    churn_label = "Ya" if prediction == 1 else "Tidak"
    st.write("Apakah Pelanggan Akan Churn?", churn_label)
