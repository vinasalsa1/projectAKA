import streamlit as st

st.title("Persamaan Gas Ideal Kalkulator")

import streamlit as st

# Konstanta gas ideal dengan sistem satuan terintegrasi
R_systems = {
    "Sistem SI": {
        "R": 8.314,
        "unit_R": "J/(mol.K)",
        "tekanan": ("kPa", "Pa"),
        "volume": ("m³", "dm³"),
        "default_pressure": 101.325,
        "default_volume": 0.0224,
        "teori": "Digunakan dalam perhitungan ilmiah, dengan satuan tekanan kPa dan volume m³"
    },
    "Sistem Atmosfer": {
        "R": 0.082057,
        "unit_R": "L.atm/(mol.K)",
        "tekanan": ("atm", "mmHg"),
        "volume": ("L", "mL"),
        "default_pressure": 1.0,
        "default_volume": 22.4,
        "teori": "Umum digunakan dalam kimia, dengan satuan tekanan atm dan volume liter"
    },
    "Sistem Teknis": {
        "R": 62.3636,
        "unit_R": "L.mmHg/(mol.K)",
        "tekanan": ("mmHg", "torr"),
        "volume": ("L", "mL"),
        "default_pressure": 760.0,
        "default_volume": 22.4,
        "teori": "Digunakan dalam aplikasi medis/laboratorium, dengan satuan mmHg"
    }
}

# ========== SETUP TAMPILAN ==========
st.set_page_config(
    page_title="Kalkulator Gas Ideal | PV=nRT",
    page_icon="🧪",
    layout="centered"
)

# Header aplikasi
st.title("🧪 Kalkulator Gas Ideal")
st.subheader("PV = nRT dengan Konsistensi Satuan Otomatis")

# ========== BAGIAN INPUT ==========
st.header("📥 Masukkan Data")

# Pilih sistem satuan
selected_system = st.selectbox(
    "Pilih sistem satuan:",
    options=list(R_systems.keys()),
    format_func=lambda x: f"{x} (R = {R_systems[x]['R']} {R_systems[x]['unit_R']})",
    help="Pilih sistem satuan yang sesuai dengan konteks perhitungan"
)

system = R_systems[selected_system]

# Tampilkan info sistem
st.info(f"""
*Sistem yang dipilih:* {selected_system}  
*Konstanta gas (R):* {system['R']} {system['unit_R']}  
*Keterangan:* {system['teori']}
""")

# Input variabel
col1, col2 = st.columns(2)

with col1:
    P = st.number_input(
        f"Tekanan (P) [{system['tekanan'][0]}]", 
        value=system["default_pressure"],
        min_value=0.0,
        step=0.01
    )
    
    V = st.number_input(
        f"Volume (V) [{system['volume'][0]}]",
        value=system["default_volume"],
        min_value=0.0,
        step=0.01
    )

with col2:
    T = st.number_input(
        "Suhu (T) [K]",
        value=273.15,
        min_value=0.0,
        step=0.1
    )
    
    n = st.number_input(
        "Jumlah mol (n) [mol]",
        value=1.0,
        min_value=0.0,
        step=0.01
    )

# ========== PROSES PERHITUNGAN ==========
def calculate_unknown(P, V, n, T, R):
    variables = [P, V, n, T]
    known_count = sum(1 for var in variables if var is not None and var > 0)
    
    if known_count == 3:
        if not n or n == 0:  # Hitung mol
            result = (P * V) / (R * T)
            formula = r"n = \frac{P \times V}{R \times T}"
            calculation = f"\frac{{{P:.4f} \times {V:.4f}}}{{{R:.6f} \times {T:.2f}}}"
            unit = "mol"
            return result, "n", unit, formula, calculation
        
        elif not P or P == 0:  # Hitung tekanan
            result = (n * R * T) / V
            formula = r"P = \frac{n \times R \times T}{V}"
            calculation = f"\frac{{{n:.4f} \times {R:.6f} \times {T:.2f}}}{{{V:.4f}}}"
            unit = system['tekanan'][0]
            return result, "P", unit, formula, calculation
        
        elif not V or V == 0:  # Hitung volume
            result = (n * R * T) / P
            formula = r"V = \frac{n \times R \times T}{P}"
            calculation = f"\frac{{{n:.4f} \times {R:.6f} \times {T:.2f}}}{{{P:.4f}}}"
            unit = system['volume'][0]
            return result, "V", unit, formula, calculation
        
        elif not T or T == 0:  # Hitung suhu
            result = (P * V) / (n * R)
            formula = r"T = \frac{P \times V}{n \times R}"
            calculation = f"\frac{{{P:.4f} \times {V:.4f}}}{{{n:.4f} \times {R:.6f}}}"
            unit = "K"
            return result, "T", unit, formula, calculation
    
    return None, None, None, None, None

# ========== BAGIAN OUTPUT ==========
if st.button("🔄 Hitung", type="primary"):
    st.header("📊 Hasil Perhitungan")
    
    result, var, unit, formula, calculation = calculate_unknown(P, V, n, T, system["R"])
    
    if result is not None:
        # Tampilkan box hasil utama
        st.success(f"*Nilai {var} = {result:.4f} {unit}*")
        
        # Tampilkan langkah perhitungan detail
        with st.expander("🧮 Detail Perhitungan", expanded=True):
            st.latex(f"{formula} = {calculation} = {result:.4f} \\text{{ {unit} }}")
            
            st.markdown("*Penjelasan:*")
            if var == "n":
                st.write("""
                Jumlah mol gas dihitung dengan membagi hasil perkalian tekanan dan volume 
                dengan hasil perkalian konstanta gas dan suhu mutlak.
                """)
            elif var == "P":
                st.write("""
                Tekanan gas dihitung dengan membagi hasil perkalian jumlah mol, konstanta gas, 
                dan suhu mutlak dengan volume.
                """)
            elif var == "V":
                st.write("""
                Volume gas dihitung dengan membagi hasil perkalian jumlah mol, konstanta gas, 
                dan suhu mutlak dengan tekanan.
                """)
            elif var == "T":
                st.write("""
                Suhu mutlak dihitung dengan membagi hasil perkalian tekanan dan volume 
                dengan hasil perkalian jumlah mol dan konstanta gas.
                """)
    else:
        st.error("Masukkan 3 variabel yang diketahui untuk menghitung variabel ke-4!")

# ========== BAGIAN TEORI ==========
with st.expander("📚 Teori Dasar", expanded=False):
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
    
    ### *Konversi Satuan Penting*
    - 1 atm = 101.325 kPa = 760 mmHg
    - 1 m³ = 1000 L
    - 0°C = 273.15 K
    
    Aplikasi ini secara otomatis menyesuaikan satuan berdasarkan sistem yang dipilih 
    untuk memastikan konsistensi dimensional dalam perhitungan.
    """)

with st.expander("🧪 Contoh Praktis", expanded=False):
    st.markdown("""
    *Contoh 1 - Menghitung Mol Gas:*
    - Tekanan = 1 atm
    - Volume = 22.4 L
    - Suhu = 273.15 K
    - R = 0.082057 L·atm/(mol·K)
    - Mol = (1 × 22.4) / (0.082057 × 273.15) ≈ 1 mol
    
    *Contoh 2 - Menghitung Tekanan:*
    - Mol = 2 mol
    - Volume = 10 L
    - Suhu = 300 K
    - R = 0.082057 L·atm/(mol·K)
    - Tekanan = (2 × 0.082057 × 300) / 10 ≈ 4.923 atm
    """)

# Catatan kaki
st.markdown("---")
st.caption("Aplikasi Kalkulator Gas Ideal © 2023 | Konsistensi satuan otomatis untuk hasil akurat")
