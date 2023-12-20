# Mengimpor library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur gaya tampilan seaborn menjadi 'dark'
sns.set(style='dark')

# Fungsi untuk membuat dataframe periode dengan jumlah total 'cnt' untuk setiap periode
def create_periode_df(df):
    sum_cnt_df = df.groupby("periode").cnt.sum().sort_values().reset_index()
    return sum_cnt_df

# Membaca dataset dari file CSV
day_df = pd.read_csv("main_data.csv")

# Mendefinisikan dataframe utama sebagai main_df
main_df = day_df

# Membuat judul header pada aplikasi Streamlit
st.header(':star: Berikut visualisasi data dari projek Bike Share Dataset :star:')

# Jawaban untuk pertanyaan nomor 1
st.subheader("Workingday VS Offday")

# Menghitung nilai workingday dan mengganti nilainya dengan label "offday" atau "weekday"
main_df['workingday'] = main_df['workingday'].apply(lambda x: 'offday' if x == 0 else 'weekday')
workingday_counts = main_df['workingday'].value_counts()

# Membuat diagram lingkaran (pie chart) untuk menampilkan persentase workingday dan offday
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(workingday_counts, labels=workingday_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Workingday VS Offday")

# Menampilkan diagram lingkaran pada aplikasi Streamlit
st.pyplot(fig)

# Jawaban untuk pertanyaan nomor 2
st.subheader("Popularitas Sewa Sepeda Berdasarkan Musim")

# Membuat diagram batang untuk menampilkan popularitas sewa sepeda berdasarkan musim
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(25, 15))
sns.barplot(x="season", y="cnt", data=main_df, ci=None)
ax.set_title("Popularitas Sewa Sepeda Berdasarkan Musim", loc="center", fontsize=50)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=35)
ax.set_ylabel(None)
ax.set_xlabel("", fontsize=10)

# Menampilkan diagram batang pada aplikasi Streamlit
st.pyplot(fig)

# Jawaban untuk pertanyaan nomor 3
st.subheader("Rental Performance in 2011 & 2012")

# Membuat dataframe periode untuk melihat penyewa sepeda per bulan
periode_df = create_periode_df(main_df)

# Membuat subplot dengan dua bagian (2011 dan 2012)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(25, 15))

# Menggambarkan diagram batang untuk penyewa sepeda di tahun 2011
sns.barplot(x="periode", y="cnt", data=periode_df.sort_values(by="periode", ascending=True).head(12), palette="Blues", ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("", fontsize=10)
ax[0].set_title("Penyewa Sepeda di 2011", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30, rotation=45)

# Menggambarkan diagram batang untuk penyewa sepeda di tahun 2012
sns.barplot(x="periode", y="cnt", data=periode_df.sort_values(by="periode", ascending=False).head(12), palette="Blues", ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("", fontsize=10)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Penyewa Sepeda di 2012", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30, rotation=45)

# Menampilkan subplot pada aplikasi Streamlit
st.pyplot(fig)

# Membuat diagram lingkaran (pie chart) untuk membandingkan kinerja penyewaan sepeda pada tahun 2011 dan 2012
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(35, 15))
st.subheader("Performance 2011 VS 2012")
yr_counts = main_df.groupby('yr')['cnt'].sum()
ax.pie(yr_counts, labels=yr_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Performance 2011 VS 2012")

# Menampilkan diagram lingkaran pada aplikasi Streamlit
st.pyplot(fig)
