import streamlit as st
import pandas as pd
import numpy as np
import random

# Fungsi mood berdasarkan cuaca
def mood_generator(row):
    if row["Kondisi"] == "Cerah" and 24 <= row["Suhu"] <= 30:
        return "Bahagia"
    elif row["Kondisi"] == "Hujan" and row["Suhu"] < 24:
        return "Sedih"
    elif row["Kondisi"] == "Berawan":
        return "Sedih dikit"
    else:
        return "Biasa saja"

# Setup
st.set_page_config(page_title="Mood Harian Berdasarkan Cuaca", page_icon="🌦️")
st.title("🌦️ Mood Harian Berdasarkan Cuaca Di Makassar")

# Membuat data acak
kondisi_options = ["Cerah", "Berawan", "Hujan"]
data = {
    "Hari": [f"Hari ke-{i+1}" for i in range(7)],
    "Suhu": np.random.randint(20, 35, size=7),
    "Kelembapan": np.random.randint(40, 100, size=7),
    "Kondisi": [random.choice(kondisi_options) for _ in range(7)]
}
df = pd.DataFrame(data)

# Tambahkan kolom mood
df["Mood"] = df.apply(mood_generator, axis=1)

# Tampilkan tabel
st.subheader("Data Cuaca dan Mood")
st.dataframe(df)

# Visualisasi
st.subheader("Suhu & Kelembapan Harian")
st.line_chart(df[["Suhu", "Kelembapan"]].set_index(df["Hari"]))

# Statistik
st.subheader("Statistik Ringkas")
st.write("Rata-rata Suhu:", f"{df['Suhu'].mean():.1f} °C")
st.write("Rata-rata Kelembapan:", f"{df['Kelembapan'].mean():.1f} %")

# Mood terbanyak
st.subheader(" Mood Terbanyak Minggu Ini")
mood_counts = df["Mood"].value_counts()
st.bar_chart(mood_counts)
