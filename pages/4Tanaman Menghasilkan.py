import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Title of the app
st.title("Regresi Linear dengan 2 Variabel Independen (3 Bulan)")

# Introduction
st.write("""
Aplikasi ini memungkinkan Anda untuk memasukkan data dua variabel independen (X1 dan X2) secara manual untuk tiga bulan (Januari hingga Maret).
Variabel X1 dan X2 bisa berupa data curah hujan, sinar matahari, atau faktor lainnya yang relevan. Variabel Y adalah hasil produksi yang ingin dianalisis.
Setelah data X1, X2, dan Y dimasukkan, aplikasi ini akan melakukan regresi linear untuk menganalisis hubungan antara variabel independen (X1 dan X2) dengan variabel dependen (Y).
Proses ini menggunakan pustaka scikit-learn dari Python, yang merupakan bagian dari teknologi Machine Learning, termasuk dalam kategori kecerdasan buatan (AI).

**Disclaimer**: Model regresi ini didasarkan pada data untuk periode tiga bulan saja (Januari hingga Maret). Oleh karena itu, hasil yang diperoleh hanya berlaku untuk periode tersebut. Akurasi model akan meningkat seiring dengan penggunaan data yang lebih banyak, misalnya data selama tiga tahun, yang memungkinkan analisis yang lebih mendalam dan hasil yang lebih representatif.
""")

# Input for dependent (y) variable
st.header("Masukkan Data Dependen (Y):")
st.write("Di bagian ini, Anda akan memasukkan nilai variabel dependen (Y) yang ingin diprediksi berdasarkan dua variabel independen (X1, X2) untuk tiga bulan (Jan - Mar).")
y_values = []

# Input for dependent variable (Y) for each month (January to March)
for month in ["Jan", "Feb", "Mar"]:
    y_val = st.number_input(f"Masukkan nilai Y untuk bulan {month}:", key=f"Y_{month}", value=0.0)
    y_values.append(y_val)

# Input for independent variables (X1, X2) for each month
st.header("Masukkan Data Independen (X1, X2):")
st.write("Di bagian ini, Anda akan memasukkan nilai dua variabel independen (X1 dan X2) yang akan digunakan untuk memprediksi nilai Y. Pastikan untuk memasukkan data untuk setiap bulan (Jan - Mar).")

X1_values, X2_values = [], []

for month in ["Jan", "Feb", "Mar"]:
    X1_val = st.number_input(f"Masukkan nilai X1 untuk bulan {month}:", key=f"X1_{month}", value=0.0)
    X2_val = st.number_input(f"Masukkan nilai X2 untuk bulan {month}:", key=f"X2_{month}", value=0.0)
    
    X1_values.append(X1_val)
    X2_values.append(X2_val)

# When the user clicks "Kalkulasi"
if st.button("Kalkulasi Regresi"):
    if len(y_values) < 3 or len(X1_values) < 3 or len(X2_values) < 3:
        st.error("Harap masukkan nilai untuk semua bulan (Jan - Mar).")
    else:
        # Convert lists to pandas DataFrame
        df = pd.DataFrame({
            "X1": X1_values,
            "X2": X2_values,
            "Y": y_values
        })
        
        # Display the input data
        st.write("Data yang dimasukkan:")
        st.write(df)

        # Prepare data for regression
        X = df[["X1", "X2"]]  # Independent variables
        y = df["Y"]    # Dependent variable

        # Train the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Make predictions
        y_pred = model.predict(X)

        # Show results
        st.subheader("Hasil Model:")
        st.write(f"Intercept: {model.intercept_}")
        st.write(f"Koefisien untuk X1: {model.coef_[0]}")
        st.write(f"Koefisien untuk X2: {model.coef_[1]}")

        # Metrics
        st.write(f"Mean Squared Error (MSE): {mean_squared_error(y, y_pred):.2f}")
        st.write(f"R^2 Score: {r2_score(y, y_pred):.2f}")

        # Plotting the results
        st.subheader("Plot Regresi Linear (X1 vs Y)")
        st.write("Grafik ini menunjukkan hubungan antara X1 dan Y dengan garis regresi linear. Hal ini akan membantu Anda memahami bagaimana X1 memengaruhi Y.")
        plt.figure(figsize=(8, 6))
        sns.regplot(x=df["X1"], y=df["Y"], line_kws={"color": "red"})
        plt.title("Regresi Linear: X1 vs Y")
        st.pyplot()

        # Plotting for X2 vs Y
        st.subheader("Plot Regresi Linear (X2 vs Y)")
        st.write("Grafik ini menunjukkan hubungan antara X2 dan Y dengan garis regresi linear. Ini menunjukkan bagaimana X2 memengaruhi Y.")
        plt.figure(figsize=(8, 6))
        sns.regplot(x=df["X2"], y=df["Y"], line_kws={"color": "red"})
        plt.title("Regresi Linear: X2 vs Y")
        st.pyplot()

        # Show predictions vs actual values
        st.subheader("Prediksi vs Nilai Sebenarnya")
        st.write("Tabel berikut menunjukkan perbandingan antara nilai yang sebenarnya (Y) dan nilai yang diprediksi oleh model. Ini memberikan gambaran tentang seberapa baik model Anda.")
        results_df = pd.DataFrame({"Aktual": y, "Prediksi": y_pred})
        st.write(results_df)
