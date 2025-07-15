import streamlit as st

# Sidebar navigasi
menu = st.tabs("Menu", ["Beranda", "Teori Gas Ideal", "Kalkulator Gas Ideal", "About Us"])

# Halaman BERANDA
if menu == "Beranda":
    st.title("Selamat Datang di Aplikasi Gas Ideal")
    st.markdown("""
    Aplikasi ini dirancang untuk membantu kamu memahami dan menghitung hubungan antar variabel 
    dalam **persamaan gas ideal PV = nRT**.

    📌 Gunakan menu di sebelah kiri untuk:
    - Mempelajari teori dasar gas ideal
    - Menghitung variabel seperti P, V, n, atau T
    - Mengenal lebih lanjut tentang aplikasi ini
    """)

# Halaman TEORI GAS IDEAL
elif menu == "Teori Gas Ideal":
    st.title("📚 Teori Gas Ideal")
    st.markdown("""
    ### Persamaan Umum Gas Ideal
    $$
    PV = nRT
    $$
    - $P$ = Tekanan gas  
    - $V$ = Volume gas  
    - $n$ = Jumlah mol  
    - $R$ = Konstanta gas  
    - $T$ = Suhu mutlak (Kelvin)  

    ### Asumsi Gas Ideal:
    - Molekul gas tidak memiliki volume
    - Tidak ada gaya tarik antar molekul
    - Tumbukan antar molekul bersifat elastis sempurna
    """)

# Halaman KALKULATOR
elif menu == "Kalkulator Gas Ideal":
    st.title("🧮 Kalkulator Gas Ideal Cerdas")
    st.subheader("PV = nRT dengan Satuan Terkoordinasi")

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
    if P and V and T and (not n or n == 0):
        return (P * V) / (R * T), "n", "mol"
    elif P and n and T and (not V or V == 0):
        return (n * R * T) / P, "V", system['volume'][0]
    elif V and n and T and (not P or P == 0):
        return (n * R * T) / V, "P", system['tekanan'][0]
    elif P and V and n and (not T or T == 0):
        return (P * V) / (n * R), "T", "K"
    return None, None, None

if st.button("Hitung Variabel"):
    result, var, unit = calculate_unknown(P, V, n, T, R)
    
    if result is not None:
        st.success(f"Nilai {var} = {result:.4f} {unit}")
        
        # Menampilkan rumus yang benar untuk setiap variabel
    if var == "n":
         st.latex(f"n = \\frac{{P \\times V}}{{R \\times T}} = \\frac{{{P:.2f} \\times {V:.2f}}}{{{R:.5f} \\times {T:.2f}}} = {result:.2f}\\ \\text{{mol}}")
    elif var == "V":
        st.latex(f"V = \\frac{{n \\times R \\times T}}{{P}} = \\frac{{{n:.2f} \\times {R:.5f} \\times {T:.2f}}}{{{P:.2f}}} = {result:.2f}\\ \\text{{{unit}}}")
    elif var == "P":
            st.latex(f"P = \\frac{{n \\times R \\times T}}{{V}} = \\frac{{{n:.2f} \\times {R:.5f} \\times {T:.2f}}}{{{V:.2f}}} = {result:.2f}\\ \\text{{{unit}}}")
    elif var == "T":
         st.latex(f"T = \\frac{{P \\times V}}{{n \\times R}} = \\frac{{{P:.2f} \\times {V:.2f}}}{{{n:.2f} \\times {R:.5f}}} = {result:.2f}\\ \\text{{K}}")
    else:
        st.warning("Masukkan 3 variabel untuk menghitung yang ke-4!")

# Penjelasan sistem satuan
with st.expander("📚 Teori Dasar"):
    st.markdown("""
    *Persamaan Gas Ideal:*
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

    st.markdown("""
    *Konsistensi Satuan:*
    Aplikasi ini secara otomatis menyesuaikan satuan tekanan dan volume 
    agar konsisten dengan satuan R yang dipilih, sehingga menghindari 
    kesalahan konversi satuan.
    """)

# Tambahkan contoh perhitungan
with st.expander("🧪 Contoh Perhitungan"):
    st.markdown("""
    *Contoh 1 (Menghitung Suhu):*
    - Sistem: Atmosfer (R = 0.082057 L·atm/(mol·K))
    - P = 1 atm
    - V = 22.4 L
    - n = 1 mol
    - T yang dihitung:
    $$
    T = \\frac{P \\times V}{n \\times R} = \\frac{1 \\times 22.4}{1 \\times 0.082057} = 273.15 \\text{ K}
    $$
    """)

