import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

import streamlit as st

# Konstanta gas ideal dalam berbagai satuan
R_values = {
    "L.atm/(mol.K)": 0.082057,
    "J/(mol.K)": 8.314,
    "L.kPa/(mol.K)": 8.314,
    "L.mmHg/(mol.K)": 62.3636,
    "L.torr/(mol.K)": 62.3636,  # 1 torr = 1 mmHg
    "L.psi/(mol.K)": 0.529990  # 1 psi = 0.068046 atm
}

# Judul aplikasi
st.title("Kalkulator Gas Ideal - PV=nRT")

# Teori Gas Ideal
st.header("Teori Gas Ideal")
st.write("""
Gas ideal adalah gas yang mengikuti hukum gas ideal, yang dinyatakan dengan persamaan:

$$
PV = nRT
$$

di mana:
- \( P \) = tekanan gas (dalam satuan yang sesuai)
- \( V \) = volume gas (dalam satuan yang sesuai)
- \( n \) = jumlah mol gas
- \( R \) = konstanta gas ideal (bervariasi tergantung satuan)
- \( T \) = suhu gas (dalam Kelvin)

Gas nyata, di sisi lain, tidak selalu mengikuti hukum gas ideal, terutama pada tekanan tinggi dan suhu rendah. Interaksi antar molekul dan volume yang ditempati oleh molekul gas itu sendiri menjadi faktor yang mempengaruhi perilaku gas nyata. Persamaan Van der Waals adalah salah satu model yang digunakan untuk menggambarkan gas nyata.
""")

# Pilih satuan R
R_unit = st.selectbox("Pilih satuan R:", list(R_values.keys()))
R = R_values[R_unit]

# Input dari pengguna
st.header("Masukkan nilai yang diketahui:")
pressure_unit = st.selectbox("Pilih satuan tekanan:", ["atm", "kPa", "mmHg", "torr", "psi"])
P = st.number_input(f"Tekanan ({pressure_unit})", min_value=0.0, format="%.2f", step=0.01)

volume_unit = st.selectbox("Pilih satuan volume:", ["L", "m³", "cm³", "mL", "ft³", "in³"])
V = st.number_input(f"Volume ({volume_unit})", min_value=0.0, format="%.2f", step=0.01)

n = st.number_input("Jumlah Mol (mol)", min_value=0.0, format="%.2f", step=0.01)

temperature_unit = st.selectbox("Pilih satuan suhu:", ["K", "°C", "°F", "R"])
T = st.number_input(f"Suhu ({temperature_unit})", min_value=0.0, format="%.2f", step=0.01)

# Konversi suhu dari Celsius ke Kelvin jika perlu
if temperature_unit == "°C":
    T += 273.15
elif temperature_unit == "°F":
    T = (T - 32) * 5/9 + 273.15  # Konversi Fahrenheit ke Kelvin
elif temperature_unit == "R":
    T = T * 5/9  # Konversi Rankine ke Kelvin

# Tombol untuk menghitung
if st.button("Hitung"):
    if P and V and T:
        # Konversi tekanan dan volume ke satuan yang sesuai
        if pressure_unit == "kPa":
            P = P / 101.325  # konversi kPa ke atm
        elif pressure_unit == "mmHg":
            P = P / 760  # konversi mmHg ke atm
        elif pressure_unit == "torr":
            P = P / 760  # konversi torr ke atm
        elif pressure_unit == "psi":
            P = P * 0.068046  # konversi psi ke atm

        if volume_unit == "m³":
            V = V * 1000  # konversi m³ ke L
        elif volume_unit == "cm³":
            V = V / 1000  # konversi cm³ ke L
        elif volume_unit == "mL":
            V = V / 1000  # konversi mL ke L
        elif volume_unit == "ft³":
            V = V * 28.3168  # konversi ft³ ke L
        elif volume_unit == "in³":
            V = V * 0.0163871  # konversi in³ ke L

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
        elif temperature_unit == "°F":
            T = (T - 273.15) * 9/5 + 32  # konversi Kelvin ke Fahrenheit
        elif temperature_unit == "R":
            T = T * 9/5  # konversi Kelvin ke Rankine
        st.success(f'Suhu (T) = {T:.2f} {temperature_unit}')
    else:
        st.error('Silakan masukkan 3 variabel untuk menghitung yang ke-4.')
