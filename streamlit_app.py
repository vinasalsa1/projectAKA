import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

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
            P_atm = P / 101.325  # konversi kPa ke atm
        elif pressure_unit == "mmHg":
            P_atm = P / 760  # konversi mmHg ke atm
        else:
            P_atm = P  # sudah dalam atm

        if volume_unit == "m³":
            V_L = V * 1000  # konversi m³ ke L
        else:
            V_L = V  # sudah dalam L

        n = (P_atm * V_L) / (R * T)
        st.success(f'Jumlah Mol (n) = {n:.2f} mol')
        
        # Hasil dalam semua satuan
        st.write(f"Tekanan dalam atm: {P_atm:.2f} atm")
        st.write(f"Tekanan dalam kPa: {P * (101.325 / 760):.2f} kPa")
        st.write(f"Tekanan dalam mmHg: {P * (760 / 760):.2f} mmHg")
        st.write(f"Volume dalam L: {V_L:.2f} L")
        st.write(f"Volume dalam m³: {V / 1000:.2f} m³")
        
    elif n and V and T:
        if volume_unit == "m³":
            V_L = V * 1000  # konversi m³ ke L
        else:
            V_L = V  # sudah dalam L
        P_atm = (n * R * T) / V_L
        st.success(f'Tekanan (P) = {P_atm:.2f} atm')
        
        # Hasil dalam semua satuan
        st.write(f"Tekanan dalam atm: {P_atm:.2f} atm")
        st.write(f"Tekanan dalam kPa: {P_atm * 101.325:.2f} kPa")
        st.write(f"Tekanan dalam mmHg: {P_atm * 760:.2f} mmHg")
        st.write(f"Volume dalam L: {V_L:.2f} L")
        st.write(f"Volume dalam m³: {V / 1000:.2f} m³")
        
    elif n and P and T:
        if pressure_unit == "kPa":
            P_atm = P / 101.325  # konversi kPa ke atm
        elif pressure_unit == "mmHg":
            P_atm = P / 760  # konversi mmHg ke atm
        else:
            P_atm = P  # sudah dalam atm
        V_L = (n * R * T) / P_atm
        st.success(f'Volume (V) = {V_L:.2f} L')
        
        # Hasil dalam semua satuan
        st.write(f"Tekanan dalam atm: {P_atm:.2f} atm")
        st.write(f"Tekanan dalam kPa: {P * (101.325 / 760):.2f} kPa")
        st.write(f"Tekanan dalam mmHg: {P * (760 / 760):.2f} mmHg")
        st.write(f"Volume dalam L: {V_L:.2f} L")
        st.write(f"Volume dalam m³: {V_L / 1000:.2f} m³")
        
    elif n and P and V:
        T = (P * V_L) / (n * R)
        if temperature_unit == "°C":
            T -= 273.15  # konversi Kelvin ke Celsius
        st.success(f'Suhu (T) = {T:.2f} {temperature_unit}')
        
        # Hasil dalam semua satuan
        st.write(f"Tekanan dalam atm: {P:.2f} atm")
        st.write(f"Tekanan dalam kPa: {P * (101.325 / 760):.2f} kPa")
        st.write(f"Tekanan dalam mmHg: {P * (760 / 760):.2f} mmHg")
        st.write(f"Volume dalam L: {V:.2f} L")
        st.write(f"Volume dalam m³: {V / 1000:.2f} m³")
    else:
        st.error('Silakan masukkan 3 variabel untuk menghitung yang ke-4.')
