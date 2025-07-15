import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

import streamlit as st

# Konstanta gas ideal
R = 0.082057  # L.atm/(mol.K)

# Judul aplikasi
st.title("Kalkulator Gas Ideal - PV=nRT")

# Input dari pengguna
st.header("Masukkan nilai yang diketahui:")
P = st.number_input("Tekanan (atm)", min_value=0.0, format="%.2f", step=0.01)
V = st.number_input("Volume (L)", min_value=0.0, format="%.2f", step=0.01)
n = st.number_input("Jumlah Mol (mol)", min_value=0.0, format="%.2f", step=0.01)
T = st.number_input("Suhu (K)", min_value=0.0, format="%.2f", step=0.01)

# Tombol untuk menghitung
if st.button("Hitung"):
    if P and V and T:
        n = (P * V) / (R * T)
        st.success(f'Jumlah Mol (n) = {n:.2f} mol')
    elif n and V and T:
        P = (n * R * T) / V
        st.success(f'Tekanan (P) = {P:.2f} atm')
    elif n and P and T:
        V = (n * R * T) / P
        st.success(f'Volume (V) = {V:.2f} L')
    elif n and P and V:
        T = (P * V) / (n * R)
        st.success(f'Suhu (T) = {T:.2f} K')
    else:
        st.error('Silakan masukkan 3 variabel untuk menghitung yang ke-4.')

