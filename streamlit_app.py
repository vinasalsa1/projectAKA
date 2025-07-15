import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

import streamlit as st

# Konstanta gas ideal dengan satuan yang saling terkait
R_systems = {
    "Sistem SI": {
        "R": 8.314,
        "unit_R": "J/(mol.K)",
        "tekanan": ("kPa", "Pa"),
        "volume": ("m³", "dm³"),
        "default_pressure": 101.325,
        "default_volume": 0.0224
    },
    "Sistem Atmosfer": {
        "R": 0.082057,
        "unit_R": "L.atm/(mol.K)",
        "tekanan": ("atm", "mmHg"),
        "volume": ("L", "mL"),
        "default_pressure": 1.0,
        "default_volume": 22.4
    },
    "Sistem Teknis": {
        "R": 62.3636,
        "unit_R": "L.mmHg/(mol.K)", 
        "tekanan": ("mmHg", "torr"),
        "volume": ("L", "mL"),
        "default_pressure": 760.0,
        "default_volume": 22.4
    }
}

# Tampilan Streamlit
st.title("Kalkulator Gas Ideal Cerdas")
st.subheader("PV = nRT dengan Satuan Terkoordinasi")

# Pilih sistem satuan berdasarkan R
selected_system = st.selectbox(
    "Pilih sistem satuan:",
    options=list(R_systems.keys()),
    format_func=lambda x: f"{x} (R = {R_systems[x]['R']} {R_systems[x]['unit_R']})"
)

# Ambil nilai dari sistem yang dipilih
system = R_systems[selected_system]
R = system["R"]
unit_R = system["unit_R"]

# Tampilkan nilai R yang dipilih
st.info(f"""
*Konstanta gas yang dipilih:*
- R = {R} {unit_R}
- Sistem: {selected_system}
""")

# Input variabel dengan satuan yang konsisten
col1, col2 = st.columns(2)

with col1:
    st.subheader("Variabel Gas")
    # Tekanan mengikuti sistem
    P = st.number_input(
        f"Tekanan (P) [{system['tekanan'][0]}]",
        value=system["default_pressure"],
        step=0.01
    )
    
    # Volume mengikuti sistem
    V = st.number_input(
        f"Volume (V) [{system['volume'][0]}]",
        value=system["default_volume"],
        step=0.01
    )

with col2:
    st.subheader("Konstanta")
    # Suhu selalu dalam Kelvin
    T = st.number_input(
        "Suhu (T) [K]",
        value=273.15,
        step=0.1
    )
    
    # Jumlah mol
    n = st.number_input(
        "Jumlah mol (n) [mol]",
        value=1.0,
        step=0.01
    )

# Hitung variabel yang belum diketahui
def calculate_unknown(P, V, n, T, R):
    if P and V and T and not n:
        return (P * V) / (R * T), "n", "mol"
    elif P and n and T and not V:
        return (n * R * T) / P, "V", system['volume'][0]
    elif V and n and T and not P:
        return (n * R * T) / V, "P", system['tekanan'][0]
    elif P and V and n and not T:
        return (P * V) / (n * R), "T", "K"

if st.button("Hitung Variabel"):
    result, var, unit = calculate_unknown(P, V, n, T, R)

    if result is not None:
        st.success(f"Nilai {var} = {result:.4f} {unit}")
        
        # Menampilkan rumus yang benar untuk T
        if var == "T":
            st.latex(r"T = \frac{P \times V}{n \times R} = \frac{" +
                     f"{P:.4f} \times {V:.4f}}{" +
                     f"{n:.4f} \times {R:.6f}} = {result:.4f} \text{{ K}}")
    else:
        st.warning("Masukkan 3 variabel untuk menghitung yang ke-4!")



# Penjelasan sistem satuan
with st.expander("📚 Penjelasan Sistem Satuan"):
    st.markdown("""
    *Koordinasi Satuan Otomatis:*
    - Sistem *SI*:
      - R = 8.314 J/(mol·K)
      - Tekanan: kPa atau Pa
      - Volume: m³ atau dm³
    
    - Sistem *Atmosfer*:
      - R = 0.082057 L·atm/(mol·K)
      - Tekanan: atm atau mmHg 
      - Volume: L atau mL
    
    - Sistem *Teknis*:
      - R = 62.3636 L·mmHg/(mol·K)
      - Tekanan: mmHg atau torr
      - Volume: L atau mL
    """)
    st.markdown("""
    *Konsistensi Satuan:*
    Aplikasi ini secara otomatis menyesuaikan satuan tekanan dan volume 
    agar konsisten dengan satuan R yang dipilih, sehingga menghindari 
    kesalahan konversi satuan.
    """)

# Tambahkan contoh perhitungan
with st.expander("🧪 Contoh Perhitungan"):
    st.markdown("""
    *Contoh 1:*
    - Sistem: SI (R = 8.314 J/(mol·K))
    - P = 101.325 kPa
    - V = 0.0224 m³
    - T = 273.15 K
    - Maka n = (101.325 × 0.0224) / (8.314 × 273.15) ≈ 1 mol
    """)
