import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Aplikasi Perhitungan Kelapa Sawit",
    page_icon="🌴",
)

# Halaman Utama
st.title("Aplikasi Perhitungan Perkebunan Kelapa Sawit 🌴")

st.subheader("Selamat Datang di Aplikasi Ini 👋")

st.write(
    """
    Aplikasi ini dirancang untuk membantu industri perkebunan kelapa sawit dalam melakukan berbagai perhitungan penting 
    yang berkaitan dengan produktivitas, biaya produksi, dan analisis performa.
    """
)

st.write("---")

st.header("Fitur Utama Aplikasi:")
st.write(
    """
    Di dalam aplikasi ini, Anda dapat:
    - Melakukan perhitungan produktivitas lahan (ton/ha)
    - Menghitung biaya produksi per hektar
    - Menganalisis ROI (Return on Investment) dan Break-even Point
    - Melakukan analisis tren hasil panen
    - Mengoptimalkan penggunaan pupuk dan tenaga kerja
    
    Silakan pilih halaman dari menu untuk memulai perhitungan Anda.
    """
)

st.write("---")

# Komentar Pengunjung
st.header("Komentar Pengunjung 💬")

# Inisialisasi session state untuk menyimpan komentar
if "comments" not in st.session_state:
    st.session_state["comments"] = []

# Input komentar dari pengguna
with st.form(key="comment_form"):
    user_name = st.text_input("Nama Anda", placeholder="Masukkan nama Anda...")
    comment = st.text_area("Komentar Anda", placeholder="Tulis komentar Anda di sini...")
    submit_button = st.form_submit_button("Kirim Komentar")

# Menyimpan komentar ke session_state
if submit_button:
    if user_name and comment:
        st.session_state["comments"].append({"name": user_name, "comment": comment})
        st.success("Komentar Anda telah dikirim!")
    else:
        st.warning("Mohon isi nama dan komentar Anda sebelum mengirim.")

# Menampilkan komentar yang sudah dikirim
if st.session_state["comments"]:
    st.subheader("Komentar Sebelumnya:")
    for idx, entry in enumerate(st.session_state["comments"]):
        st.write(f"**{entry['name']}**: {entry['comment']}")
else:
    st.info("Belum ada komentar. Jadilah yang pertama memberikan komentar!")

st.write("---")

st.header("Tentang Kami")
st.write(
    """
    Kami berkomitmen untuk mendukung industri perkebunan kelapa sawit melalui teknologi yang mudah digunakan 
    dan analisis berbasis data. Hubungi kami untuk kolaborasi atau informasi lebih lanjut.
    """
)

st.write("---")

st.write("✨ **Versi Beta - Dikembangkan menggunakan Streamlit** ✨")
