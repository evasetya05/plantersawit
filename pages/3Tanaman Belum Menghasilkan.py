import streamlit as st

# Initialize session_state variables if they don't exist
if 'HA' not in st.session_state:
    st.session_state.HA = 0.0
if 'rotasi' not in st.session_state:
    st.session_state.rotasi = 0.0
if 'prestasi_kerja' not in st.session_state:
    st.session_state.prestasi_kerja = 0.1

# Judul Halaman
st.title("Perhitungan Keperluan Karyawan")

# Penjelasan singkat
st.write("Aplikasi ini membantu menghitung keperluan hari kerja berdasarkan data yang dimasukkan.")

# Input dari pengguna
st.header("Masukkan Data:")
HA = st.number_input(
    "Masukkan nilai HA (Hektar):",
    key="HA",
    value=st.session_state.HA,
    step=0.1,
    format="%.2f",
    help="Masukkan luas lahan dalam hektar."
)
rotasi = st.number_input(
    "Masukkan nilai Rotasi (frekuensi pengerjaan per tahun):",
    key="rotasi",
    value=st.session_state.rotasi,
    step=0.1,
    format="%.2f",
    help="Masukkan jumlah rotasi per tahun."
)
prestasi_kerja = st.number_input(
    "Masukkan Prestasi Kerja (hektar per hari):",
    key="prestasi_kerja",
    value=st.session_state.prestasi_kerja,
    step=0.1,
    min_value=0.1,
    format="%.2f",
    help="Masukkan produktivitas kerja per hari (minimal 0.1 hektar)."
)

# Button untuk kalkulasi
if st.button("Kalkulasi"):
    if HA == 0 or rotasi == 0:
        st.error("Harap masukkan nilai HA dan Rotasi yang lebih besar dari 0 untuk melanjutkan kalkulasi.")
    else:
        # Perhitungan
        ha_dikerjakan_setahun = HA * rotasi
        keperluan_hari_kerja_setahun = ha_dikerjakan_setahun / prestasi_kerja
        
        # Keperluan HK 1 bulan dan keperluan karyawan per hari
        keperluan_hk_1_bulan = keperluan_hari_kerja_setahun / 12
        keperluan_karyawan_satu_hari = keperluan_hk_1_bulan / 25  # Anggap 25 hari kerja dalam sebulan
        
        # Rasio keperluan karyawan untuk HA
        rasio_keperluan_karyawan_per_ha = HA / keperluan_karyawan_satu_hari

        # Output hasil dengan thousand separator
        st.subheader("Hasil Kalkulasi:")
        st.write(f"- **HA yang dikerjakan setahun (Ha x Rotasi):** {ha_dikerjakan_setahun:,.2f} hektar")
        st.write(f"- **Keperluan hari kerja setahun (Ha / prestasi kerja):** {keperluan_hari_kerja_setahun:,.2f} hari kerja")
        st.write(f"- **Keperluan HK 1 bulan (Keperluan hari kerja setahun / 12 bulan):** {keperluan_hk_1_bulan:,.2f} HK")
        st.write(f"- **Keperluan HK satu hari (keperluan HK 1 bulan / 25 hari kerja):** {keperluan_karyawan_satu_hari:,.2f} karyawan")
        st.write(f"- **ratio karyawan berbanding Ha untuk {HA} hektar. Yaitu: 1 orang mengerjakan** {int(rasio_keperluan_karyawan_per_ha)} hektar atau disebut land to man ratio")

