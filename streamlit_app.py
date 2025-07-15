import streamlit as st

st.markdown("""
<style>
/* === LATAR BELAKANG & TEKS === */
.stApp {
    background: linear(to bottom, #FFFFFF, #FFFFF)F;  /* Warna klasik krem */
    color: #3e2723;  /* Coklat tua klasik */
    font-family: 'Georgia', serif;
    font-size: 16px;
    padding: 1rem;
}

/* === HEADER & TITLE === */
h1, h2, h3, .stTabs [role="tab"] {
    color: #00008B;
}

/* === TAB STYLE === */
.stTabs [role="tab"] {
    background-color: #f3e5ab;
    border-radius: 8px 8px 0 0;
    padding: 0.5rem 1.5rem;
    margin-right: 8px;
    font-weight: bold;
    color: #3e2723;
    border: 1px solid #d7ccc8;
}

.stTabs [role="tab"][aria-selected="true"] {
    background-color: #fff8e1;
    border-bottom: none;
    border-top: 3px solid #8d6e63;
}

/* === BUTTON STYLE === */
button[kind="primary"] {
    background-color: #a1887f;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
}

button[kind="primary"]:hover {
    background-color: #8d6e63;
}

/* === INFO BOX === */
[data-testid="stInfo"] {
    background-color: #ffecb3;
    color: #4e342e;
    border-left: 5px solid #8d6e63;
    padding: 1rem;
}

/* === EXPANDER === */
.streamlit-expanderHeader {
    background-color: #f5f5f5;
    color: #5d4037;
    font-weight: bold;
    padding: 0.5rem;
    border: 1px solid #d7ccc8;
    border-radius: 4px;
}

/* === INPUT FIELDS === */
input, select, textarea {
    background-color: #fff8e1;
    border: 1px solid #d7ccc8;
    border-radius: 6px;
    padding: 0.4rem;
}

/* === CONTAINER === */
.block-container {
    padding: 2rem 3rem;
}
</style>
""", unsafe_allow_html=True)



# Ubah ke tampilan layar penuh
st.set_page_config(layout="wide", page_title="Kalkulator Gas Ideal", page_icon="🧪")

tab1, tab2, tab3, tab4 = st.tabs(["🏠 Beranda", "📘 Teori", "🧮 Kalkulator", "ℹ️ About Us"])

with tab1:
    st.header("🏠 Selamat Datang di Aplikasi Gas Ideal")
    st.write("""
    Aplikasi ini membantu kamu memahami dan menghitung hubungan antara tekanan, volume, suhu, dan jumlah mol menggunakan **persamaan gas ideal**.
    Silakan navigasi ke tab 'Kalkulator' untuk mulai perhitungan.
    """)

with tab2:
    st.header("Teori Gas Ideal")
    # konten Teori

with tab3:
    st.header("Kalkulator Gas Ideal")
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
    
    

with tab4:
    st.header("Tentang Kami")
    # konten about


