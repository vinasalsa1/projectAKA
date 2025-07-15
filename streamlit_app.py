import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

import streamlit as st

# Judul aplikasi
st.title("Kalkulator Persamaan Gas Ideal - PV=nRT")

# Fungsi untuk mengonversi satuan
def convert_pressure(value, unit):
    if unit == "atm":
        return value
    elif unit == "Pa":
        return value / 101325
    elif unit == "mmHg":
        return value / 760

def convert_volume(value, unit):
    if unit == "liter":
        return value
    elif unit == "m3":
        return value * 1000

def convert_temperature(value, unit):
    if unit == "K":
        return value
    elif unit == "C":
        return value + 273.15

# Input variabel
P = st.number_input("Tekanan (P):", min_value=0.0)
P_unit = st.selectbox("Satuan Tekanan:", ["atm", "Pa", "mmHg"])

V = st.number_input("Volume (V):", min_value=0.0)
V_unit = st.selectbox("Satuan Volume:", ["liter", "m3"])

n = st.number_input("Jumlah zat (n) dalam mol:", min_value=0.0)

T = st.number_input("Suhu (T):", min_value=0.0)
T_unit = st.selectbox("Satuan Suhu:", ["K", "C"])

# Pilihan variabel yang ingin dihitung
option = st.selectbox("Pilih variabel yang ingin dihitung:", ["P", "V", "n", "T"])

# Menghitung berdasarkan pilihan
if st.button("Hitung"):
    # Konversi satuan
    P_converted = convert_pressure(P, P_unit)
    V_converted = convert_volume(V, V_unit)
    T_converted = convert_temperature(T, T_unit)

    R = 0.082057  # Konstanta gas ideal

    if option == "P":
        result = n * R * T_converted / V_converted
        st.write(f"Hasil: Tekanan (P) = {result:.2f} atm")
    elif option == "V":
        result = n * R * T_converted / P_converted
        st.write(f"Hasil: Volume (V) = {result:.2f} liter")
    elif option == "n":
        result = P_converted * V_converted / (R * T_converted)
        st.write(f"Hasil: Jumlah zat (n) = {result:.2f} mol")
    elif option == "T":
        result = P_converted * V_converted / (n * R)
        st.write(f"Hasil: Suhu (T) = {result:.2f} K")
