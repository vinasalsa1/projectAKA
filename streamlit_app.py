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
    background-color: #1e3a8a;  /* dark blue (tidak aktif) */
    border-radius: 8px 8px 0 0;
    padding: 0.5rem 1.5rem;
    margin-right: 8px;
    font-weight: bold;
    color: white;
    border: 1px solid #0a1f44;
    transition: all 0.3s ease-in-out;
}

.stTabs [role="tab"][aria-selected="true"] {
    background-color: #172554;  /* lebih gelap saat aktif */
    color: #ffffff;
    border-bottom: 3px solid #60a5fa;
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
    st.title("IDEAL GAS CALCULATOR")  # Judul besar

    st.subheader("Selamat datang di aplikasi interaktif perhitungan gas ideal.")

    st.write("""
        Aplikasi ini dikembangkan untuk membantu Anda memahami konsep dasar termodinamika 
        melalui persamaan gas ideal. Persamaan ini menyatakan hubungan antara tekanan (P), 
        volume (V), suhu (T), dan jumlah mol gas (n).
    """)

    st.latex("PV = nRT")  # Menampilkan persamaan secara matematis

    st.write("""
        Dengan antarmuka yang sederhana dan sistem satuan yang konsisten, 
        Anda dapat melakukan simulasi dan perhitungan ilmiah secara lebih akurat dan efisien.
        Silakan gunakan tab **Kalkulator** untuk memulai perhitungan.
    """)


with tab2:
    st.header("📘 Teori Gas Ideal")

    st.write("""
    **Termodinamika** adalah cabang ilmu fisika yang mempelajari hubungan antara energi, panas, dan kerja dalam suatu sistem. 
    Ilmu ini berfokus pada sifat-sifat makroskopik zat, seperti suhu, tekanan, dan volume, yang dapat diukur secara langsung.
    Salah satu konsep dasar dalam termodinamika adalah **persamaan keadaan**, yang menjelaskan hubungan antara sifat-sifat 
    tersebut dalam bentuk matematis.

    Salah satu persamaan keadaan yang paling sederhana dan paling umum digunakan adalah **persamaan gas ideal**:
    """)

    st.latex("PV = nRT")

    st.write("""
    Menurut Nurbury (2000:226), gas dikatakan **ideal** jika gaya tarik-menarik antar molekulnya dapat diabaikan. 
    Dalam praktiknya, pendekatan gas ideal sangat berguna untuk memodelkan perilaku gas di berbagai kondisi.

    Untuk memahami perilaku gas, perlu diketahui hubungan antara **massa gas**, **volume**, dan **jumlah mol**. 
    Jumlah mol ($n$) adalah perbandingan antara massa total gas dengan massa molekul relatif gas tersebut.
    
    Misalnya, saat udara dipompa ke dalam balon atau alat suntik (*syringe*), semakin banyak gas yang dimasukkan, 
    semakin besar volumenya (dengan asumsi suhu dan tekanan tetap). Hubungan ini bersifat **linier**, 
    dan dapat dijelaskan dengan memasukkan **konstanta gas** dan menyusun hubungan menjadi:
    
    $$ PV = nRT $$

    Jika tekanan ($P$), suhu ($T$), dan volume ($V$) diketahui, maka jumlah mol gas dapat dihitung. 
    Hal ini penting, terutama dalam eksperimen-eksperimen yang melibatkan wadah tertutup seperti tabung suntik atau bola udara.

    Penelitian sebelumnya telah banyak membahas hubungan dasar ini, namun pengembangan lebih lanjut mengenai 
    **jumlah mol dalam sistem volume tetap atau suhu tetap** menggunakan **persamaan gas ideal**, serta 
    hukum **Boyle–Mariotte** dan **Gay–Lussac**, membuka peluang baru untuk kajian lebih mendalam dalam sistem tertutup.
    """)

    st.markdown("*Sumber: SOUISA,M. 2011. Penentuan Jumlah Mol Udara dalam Silinder Bola dengan Menggunakan Hukum Boyle-Meriotte. 5(1). Hal 11-45.*")


with tab3:
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
        st.subheader(" ")
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
    st.header("ℹ️ About Us")

    st.subheader("Kelompok 8 – Mata Kuliah Logika Pemrograman Komputer")

    st.write("""
    Aplikasi ini dikembangkan oleh **Kelompok 8** sebagai bagian dari tugas proyek pada mata kuliah *Logika Pemrograman Komputer*  
    Program Studi **D3 Analisis Kimia**, dengan tujuan untuk menerapkan konsep logika pemrograman dalam konteks ilmiah yang relevan 
    dengan bidang keilmuan kami.

    **Anggota Kelompok 8:**
    1. Aulia Cahyani 
    2. Firdaus Cahya Ramadhan
    3. Muhammad Daffa Faliha
    4. Praya Athalla Pantow
    5. Vina Salsabila Karina Effendi

    ---
    """)

    st.subheader("Tujuan Pengembangan Aplikasi")

    st.write("""
    Aplikasi **Kalkulator Gas Ideal** ini bertujuan untuk membantu pengguna, baik mahasiswa, dosen, maupun praktisi kimia, 
    dalam memahami dan menghitung hubungan antara tekanan, volume, suhu, dan jumlah mol suatu gas berdasarkan **persamaan gas ideal (PV = nRT)**.  
    Dengan antarmuka yang interaktif dan sistem satuan yang konsisten, aplikasi ini diharapkan mampu mempermudah proses simulasi dan perhitungan 
    pada berbagai kondisi eksperimen, khususnya dalam konteks pembelajaran maupun penelitian dasar di bidang kimia analitik dan termodinamika.

    Aplikasi ini dirancang dengan mengintegrasikan logika pemrograman dasar menggunakan bahasa Python dan modul Streamlit, 
    sehingga tidak hanya mendukung penguatan pemahaman konsep gas ideal, tetapi juga menjadi media pembelajaran pengembangan aplikasi berbasis data ilmiah.
    """)

