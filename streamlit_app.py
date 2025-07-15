import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

import streamlit as st

# Konstanta gas ideal dalam berbagai satuan
R_values = {
    "L.atm/(mol.K)": 0.082057,
    "J/(mol.K)": 8.314,
    "L.kPa/(mol.K)": 8.314,
    "L.mmHg/(mol.K)": 62.3636,
    "L.torr/(mol.K)": 62.3636,
    "L.psi/(mol.K)": 0.529990
}

# Judul aplikasi
st.title("Kalkulator Gas Ideal - PV=nRT")
st.subheader("Dengan Detail Proses Perhitungan")

# ========== TEORI ==========
with st.expander("📚 Teori Dasar"):
    st.markdown("""
    *Hukum Gas Ideal:*
    $$
    PV = nRT
    $$

    *Konversi Satuan Temperatur:*
    - °C → K: \( T_K = T_{°C} + 273.15 \)
    - °F → K: \( T_K = \frac{(T_{°F} - 32) × 5}{9} + 273.15 \)
    - R  → K: \( T_K = T_R × \frac{5}{9} \)
    """)

# ========== INPUT USER ==========
st.header("Masukkan Nilai")

R_unit = st.selectbox("Pilih satuan R:", list(R_values.keys()))
R = R_values[R_unit]
st.info(f"*Nilai R yang digunakan:* {R:.6f} {R_unit}")

col1, col2 = st.columns(2)
with col1:
    P = st.number_input("Tekanan:", min_value=0.0, value=1.0, step=0.01)
    pressure_unit = st.selectbox("Satuan tekanan:", ["atm", "kPa", "mmHg", "torr", "psi"])
    
    V = st.number_input("Volume:", min_value=0.0, value=1.0, step=0.01)
    volume_unit = st.selectbox("Satuan volume:", ["L", "m³", "cm³", "mL", "ft³", "in³"])

with col2:
    n = st.number_input("Jumlah mol (n):", min_value=0.0, value=1.0, step=0.01)
    
    T = st.number_input("Suhu:", min_value=0.0, value=273.15, step=0.01)
    temperature_unit = st.selectbox("Satuan suhu:", ["K", "°C", "°F", "R"])

# ========== KONVERSI SATUAN ==========
with st.expander("🔍 Proses Konversi Satuan"):
    st.subheader("Nilai Sebelum Konversi")
    st.write(f"- Tekanan (P): {P} {pressure_unit}")
    st.write(f"- Volume (V): {V} {volume_unit}")
    st.write(f"- Suhu (T): {T} {temperature_unit}")

    # Konversi suhu ke Kelvin
    original_T = T
    if temperature_unit == "°C":
        T += 273.15
        st.write(f"Konversi suhu: {original_T}°C + 273.15 = {T:.2f} K")
    elif temperature_unit == "°F":
        T = (T - 32) * 5/9 + 273.15
        st.write(f"Konversi suhu: ({original_T}°F - 32) × 5/9 + 273.15 = {T:.2f} K")
    elif temperature_unit == "R":
        T = T * 5/9
        st.write(f"Konversi suhu: {original_T}°R × 5/9 = {T:.2f} K")
    else:
        st.write("Suhu sudah dalam Kelvin (K)")

    original_P = P
    # Konversi tekanan ke atm (standar perhitungan)
    if pressure_unit == "kPa":
        P = P / 101.325
        st.write(f"Konversi tekanan: {original_P} kPa / 101.325 = {P:.6f} atm")
    elif pressure_unit == "mmHg":
        P = P / 760
        st.write(f"Konversi tekanan: {original_P} mmHg / 760 = {P:.6f} atm")
    elif pressure_unit == "torr":
        P = P / 760
        st.write(f"Konversi tekanan: {original_P} torr / 760 = {P:.6f} atm")
    elif pressure_unit == "psi":
        P = P * 0.068046
        st.write(f"Konversi tekanan: {original_P} psi × 0.068046 = {P:.6f} atm") 
    else:
        st.write("Tekanan sudah dalam atm")

    original_V = V
    # Konversi volume ke Liter
    if volume_unit == "m³":
        V = V * 1000
        st.write(f"Konversi volume: {original_V} m³ × 1000 = {V:.2f} L")
    elif volume_unit == "cm³":
        V = V / 1000
        st.write(f"Konversi volume: {original_V} cm³ / 1000 = {V:.2f} L")
    elif volume_unit == "mL":
        V = V / 1000
        st.write(f"Konversi volume: {original_V} mL / 1000 = {V:.2f} L")
    elif volume_unit == "ft³":
        V = V * 28.3168
        st.write(f"Konversi volume: {original_V} ft³ × 28.3168 = {V:.2f} L")
    elif volume_unit == "in³":
        V = V * 0.0163871
        st.write(f"Konversi volume: {original_V} in³ × 0.0163871 = {V:.2f} L")
    else:
        st.write("Volume sudah dalam Liter")

# ========== PROSES HITUNG ==========
if st.button("🖩 Hitung"):
    st.header("Hasil Perhitungan")
    
    with st.expander("📝 Langkah Kalkulasi", expanded=True):
        if P and V and T:
            # Hitung mol (n)
            calculated_n = (P * V) / (R * T)
            st.latex(f"n = \\frac{{P × V}}{{R × T}} = \\frac{{{P:.4f} × {V:.4f}}}{{{R:.6f} × {T:.2f}}} = {calculated_n:.6f} \\text{{ mol}}")
            
        elif n and V and T:
            # Hitung tekanan (P)
            calculated_P = (n * R * T) / V
            st.latex(f"P = \\frac{{n × R × T}}{{V}} = \\frac{{{n:.4f} × {R:.6f} × {T:.2f}}}{{{V:.4f}}} = {calculated_P:.6f} \\text{{ atm}}")
            
            # Konversi kembali ke satuan asli
            if pressure_unit == "kPa":
                final_P = calculated_P * 101.325
                st.write(f"Konversi ke kPa: {calculated_P:.6f} atm × 101.325 = {final_P:.6f} kPa")
            elif pressure_unit == "mmHg":
                final_P = calculated_P * 760
                st.write(f"Konversi ke mmHg: {calculated_P:.6f} atm × 760 = {final_P:.6f} mmHg")
            elif pressure_unit == "torr":
                final_P = calculated_P * 760
                st.write(f"Konversi ke torr: {calculated_P:.6f} atm × 760 = {final_P:.6f} torr")
            elif pressure_unit == "psi":
                final_P = calculated_P / 0.068046
                st.write(f"Konversi ke psi: {calculated_P:.6f} atm / 0.068046 = {final_P:.6f} psi")
            else:
                final_P = calculated_P
            
        elif n and P and T:
            # Hitung volume (V)
            calculated_V = (n * R * T) / P
            st.latex(f"V = \\frac{{n × R × T}}{{P}} = \\frac{{{n:.4f} × {R:.6f} × {T:.2f}}}{{{P:.6f}}} = {calculated_V:.6f} \\text{{ L}}")
            
            # Konversi kembali ke satuan asli
            if volume_unit == "m³":
                final_V = calculated_V / 1000
                st.write(f"Konversi ke m³: {calculated_V:.6f} L / 1000 = {final_V:.6f} m³")
            elif volume_unit == "cm³":
                final_V = calculated_V * 1000
                st.write(f"Konversi ke cm³: {calculated_V:.6f} L × 1000 = {final_V:.6f} cm³")
            elif volume_unit == "mL":
                final_V = calculated_V * 1000
                st.write(f"Konversi ke mL: {calculated_V:.6f} L × 1000 = {final_V:.6f} mL")
            elif volume_unit == "ft³":
                final_V = calculated_V / 28.3168
                st.write(f"Konversi ke ft³: {calculated_V:.6f} L / 28.3168 = {final_V:.6f} ft³")
            elif volume_unit == "in³":
                final_V = calculated_V / 0.0163871
                st.write(f"Konversi ke in³: {calculated_V:.6f} L / 0.0163871 = {final_V:.6f} in³")
            else:
                final_V = calculated_V
                
        elif n and P and V:
            # Hitung suhu (T)
            calculated_T = (P * V) / (n * R)
            st.latex(f"T = \\frac{{P × V}}{{n × R}} = \\frac{{{P:.6f} × {V:.4f}}}{{{n:.4f} × {R:.6f}}} = {calculated_T:.6f} \\text{{ K}}")
            
            # Konversi kembali ke satuan asli
            if temperature_unit == "°C":
                final_T = calculated_T - 273.15
                st.write(f"Konversi ke °C: {calculated_T:.6f} K - 273.15 = {final_T:.6f} °C")
            elif temperature_unit == "°F":
                final_T = (calculated_T - 273.15) * 9/5 + 32
                st.write(f"Konversi ke °F: ({calculated_T:.6f} K - 273.15) × 9/5 + 32 = {final_T:.6f} °F")
            elif temperature_unit == "R":
                final_T = calculated_T * 9/5
                st.write(f"Konversi ke °R: {calculated_T:.6f} K × 9/5 = {final_T:.6f} °R")
            else:
                final_T = calculated_T
        else:
            st.error("Masukkan 3 variabel untuk menghitung yang ke-4!")

    # Tampilkan hasil akhir dalam box khusus
    st.success("*Hasil Akhir:*")
    
    if P and V and T:
        st.metric(label="Jumlah Mol (n)", value=f"{calculated_n:.6f} mol")
    elif n and V and T:
        st.metric(label=f"Tekanan (P)", value=f"{final_P:.6f} {pressure_unit}")
    elif n and P and T:
        st.metric(label="Volume (V)", value=f"{final_V:.6f} {volume_unit}")
    elif n and P and V:
        st.metric(label="Suhu (T)", value=f"{final_T:.6f} {temperature_unit}")
