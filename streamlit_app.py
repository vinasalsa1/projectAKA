import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

import streamlit as st

# Konstanta gas ideal dalam berbagai satuan
R_values = {
    "L.atm/(mol.K)": 0.082057,
    "J/(mol.K)": 8.314,
    "L.kPa/(mol.K)": 8.314,
    "L.mmHg/(mol.K)": 62.3636
}

# Judul aplikasi
st.title("Kalkulator Gas Ideal - PV=nRT")

# Pilih satuan R
R_unit = st.selectbox("Pilih satuan R:", list(R_values.keys()))
R = R_values[R_unit]

# Input dari pengguna
st.header("Masukkan nilai yang diketahui:")
pressure_unit = st.selectbox("Pilih satuan tekanan:", ["atm", "kPa", "mmHg"])
P = st.number_input(f"Tekanan ({pressure_unit})", min_value=0.0, format="%.2f", step=0.01)

volume_unit = st.selectbox("Pilih satuan volume:", ["L", "m³"])
V = st.number_input(f"Volume ({volume_unit})", min_value=0.0, format="%.2f", step=0.01)

n = st.number_input("Jumlah Mol (mol)", min_value=0.0, format="%.2f", step=0.01)

temperature_unit = st.selectbox("Pilih satuan suhu:", ["K", "°C"])
T = st.number_input(f"Suhu ({temperature_unit})", min_value=0.0, format="%.2f", step=0.01)

# Konversi suhu dari Celsius ke Kelvin jika perlu
if temperature_unit == "°C":
    T += 273.15

# Tombol untuk menghitung
if st.button("Hitung"):
    if P and V and T:
        # Konversi tekanan dan volume ke satuan yang sesuai
        if pressure_unit == "kPa":
            P = P / 101.325  # konversi kPa ke atm
        elif pressure_unit == "mmHg":
            P = P / 760  # konversi mmHg ke atm

        if volume_unit == "m³":
            V = V * 1000  # konversi m³ ke L

        n = (P * V) / (R * T)
        st.success(f'Jumlah Mol (n) = {n:.2f} mol')
    elif n and V and T:
        if volume_unit == "m³":
            V = V * 1000  # konversi m³ ke L
        P = (n * R * T) / V
        st.success(f'Tekanan (P) = {P:.2f} {pressure_unit}')
    elif n and P and T:
        if pressure_unit == "kPa":
            P = P / 101.325  # konversi kPa ke atm
        V = (n * R * T) / P
        st.success(f'Volume (V) = {V:.2f} {volume_unit}')
    elif n and P and V:
        T = (P * V) / (n * R)
        if temperature_unit == "°C":
            T -= 273.15  # konversi Kelvin ke Celsius
        st.success(f'Suhu (T) = {T:.2f} {temperature_unit}')
    else:
        st.error('Silakan masukkan 3 variabel untuk menghitung yang ke-4.')

