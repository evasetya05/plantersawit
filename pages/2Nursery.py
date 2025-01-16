import streamlit as st

# Judul aplikasi
st.title("Aplikasi Perhitungan Nursery Kelapa Sawit 🌱")

# Perhitungan Kebutuhan Bibit
st.header("Perhitungan Kebutuhan Bibit")
luas_area = st.number_input("Masukkan luas area (ha):", min_value=0.0, format="%.2f")
bibit_per_hektar = st.number_input("Masukkan jumlah bibit per hektar:", min_value=1, max_value=2000)
if st.button("Hitung Kebutuhan Bibit"):
    kebutuhan_bibit = luas_area * bibit_per_hektar
    st.success(f"Jumlah bibit yang dibutuhkan: {kebutuhan_bibit} bibit")

# Perhitungan Biaya Produksi per Bibit
st.header("Perhitungan Biaya Produksi per Bibit")
total_biaya = st.number_input("Masukkan total biaya nursery (Rp):", min_value=0.0)
jumlah_bibit = st.number_input("Masukkan jumlah bibit yang diproduksi:", min_value=1)
if st.button("Hitung Biaya Produksi"):
    biaya_per_bibit = total_biaya / jumlah_bibit
    st.success(f"Biaya produksi per bibit: Rp {biaya_per_bibit:.2f}")

# Perhitungan Waktu Perawatan Bibit
st.header("Perhitungan Waktu Perawatan Bibit")
waktu_mulai = st.date_input("Tanggal mulai perawatan")
waktu_tanam = st.date_input("Tanggal tanam di kebun")
if st.button("Hitung Waktu Perawatan"):
    waktu_perawatan = (waktu_tanam - waktu_mulai).days / 30  # Menghitung dalam bulan
    st.success(f"Waktu perawatan bibit: {waktu_perawatan:.1f} bulan")

# Perhitungan Kebutuhan Air dan Pupuk
st.header("Perhitungan Kebutuhan Air dan Pupuk")
kebutuhan_air_per_bibit = st.number_input("Masukkan kebutuhan air per bibit per minggu (liter):", min_value=0.0)
durasi_perawatan = st.number_input("Masukkan durasi perawatan (minggu):", min_value=1)
if st.button("Hitung Kebutuhan Air"):
    total_air = kebutuhan_air_per_bibit * durasi_perawatan
    st.success(f"Total kebutuhan air per bibit: {total_air:.2f} liter")

# Perhitungan Pendapatan Potensial
st.header("Perhitungan Pendapatan dari Penjualan Bibit")
jumlah_bibit_terjual = st.number_input("Masukkan jumlah bibit yang terjual:", min_value=0)
harga_per_bibit = st.number_input("Masukkan harga per bibit (Rp):", min_value=0)
if st.button("Hitung Pendapatan"):
    pendapatan = jumlah_bibit_terjual * harga_per_bibit
    st.success(f"Pendapatan dari penjualan bibit: Rp {pendapatan:,.2f}")
