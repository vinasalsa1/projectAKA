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
st.title("🧪 Kalkulator Gas Ideal Cerdas")
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

# Input variabel
col1, col2 = st.columns(2)

with col1:
    st.subheader("Variabel Gas")
    P = st.number_input(
        f"Tekanan (P) [{system['tekanan'][0]}]",
        value=system["default_pressure"],
        step=0.01
    )
    V = st.number_input(
        f"Volume (V) [{system['volume'][0]}]", 
        value=system["default_volume"],
        step=0.01
    )

with col2:
    st.subheader("Konstanta")
    T = st.number_input("Suhu (T) [K]", value=273.15, step=0.1)
    n = st.number_input("Jumlah mol (n) [mol]", value=1.0, step=0.01)

# Fungsi perhitungan
def calculate_unknown(P, V, n, T, R):
    if P and V and T and not n:
        return (P * V) / (R * T), "n", "mol"
    elif P and n and T and not V:
        return (n * R * T) / P, "V", system['volume'][0]
    elif V and n and T and not P:
        return (n * R * T) / V, "P", system['tekanan'][0] 
    elif P and V and n and not T:
        return (P * V) / (n * R), "T", "K"
    return None, None, None

# Tombol hitung dan tampilan hasil
if st.button("🔄 Hitung", type="primary"):
    st.header("📊 Hasil Perhitungan")
    
    result, var, unit = calculate_unknown(P, V, n, T, R)
    
    if result is not None:
        st.success(f"*Nilai {var} = {result:.4f} {unit}*")
        
        with st.expander("🧮 Langkah Perhitungan", expanded=True):
            if var == "n":
                st.latex(r"n = \frac{P \times V}{R \times T} = \frac{" +
                         f"{P:.4f} \times {V:.4f}}{" +
                         f"{R:.6f} \times {T:.2f}}} = {result:.4f} \text{{ mol}}")
            
            elif var == "V":
                st.latex(r"V = \frac{n \times R \times T}{P} = \frac{" +
                         f"{n:.4f} \times {R:.6f} \times {T:.2f}}{" +
                         f"{P:.4f}}} = {result:.4f} \text{{ {unit}}}")
            
            elif var == "P":
                st.latex(r"P = \frac{n \times R \times T}{V} = \frac{" +
                         f"{n:.4f} \times {R:.6f} \times {T:.2f}}{" +
                         f"{V:.4f}}} = {result:.4f} \text{{ {unit}}}")
                         
            elif var == "T":
                st.latex(r"T = \frac{P \times V}{n \times R} = \frac{" +
                         f"{P:.4f} \times {V:.4f}}{" +
                         f"{n:.4f} \times {R:.6f}}} = {result:.4f} \text{{ K}}")
            
            st.markdown("*Penjelasan:*")
            st.write(f"Variabel {var} dihitung menggunakan rumus dasar gas ideal PV = nRT")
    else:
        st.error("Harap masukkan 3 variabel untuk menghitung variabel ke-4!")

# Teori dan contoh
with st.expander("📚 Teori Dasar"):
    st.markdown("""
    ### *Persamaan Gas Ideal*
    $$
    PV = nRT
    $$
    
    Dimana:
    - $P$ = Tekanan gas
    - $V$ = Volume gas
    - $n$ = Jumlah mol gas
    - $R$ = Konstanta gas ideal
    - $T$ = Suhu mutlak (Kelvin)
    """)

with st.expander("🧪 Contoh Praktis"):
    st.markdown("""
    *Contoh Perhitungan Suhu:*
    - Tekanan = 1 atm
    - Volume = 22.4 L
    - Mol = 1 mol
    - R = 0.082057 L·atm/(mol·K)
    - Suhu:
    $$
    T = \frac{1 \times 22.4}{1 \times 0.082057} = 273.15 \text{ K}
    $$
    """)
