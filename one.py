import streamlit as st
import pandas as pd
import base64
from io import BytesIO

st.set_page_config(page_title="Demo HTML Styling", layout="wide")
st.title("📈 Data Insight")

#import streamlit as st
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')

# Buat data
bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
harga_cabai = [48611, 46667, 47111, 47778, 49028, 47733, 48056, 47333, 46528, 46667, 43022, 41250]

# Buat plot
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title("Contoh Grafik")

plt.bar(bulan, harga_cabai)
# Menambahkan judul dan label sumbu
plt.title('Grafik Harga Cabai Th. 2023')
plt.xlabel('Bulan')
plt.ylabel('Rupiah')
# Membatas nilai sumbu-x dan y
plt.xlim(0, 13)
plt.ylim(40000, 50000)

# Menampilkan semua sumbu
plt.xticks(bulan)

# Menambahkan label angka di atas setiap bar plot
for i, value in enumerate(harga_cabai, start=1):
    plt.annotate(str(value), xy=(i, value), xytext=(0, 3),
                 textcoords='offset points', ha='center', fontsize=8, color='darkblue')

fig = plt.gcf()   # ambil current figure

#----fig2--------------------
# Buat data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Buat plot
fig2, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Grafik Pertama")

# Tampilkan di Streamlit
# st.pyplot(fig2)
#------------------------

# Tampilkan di Streamlit
# st.pyplot(fig)

#-------------------------------------------------------
paragraf = """
Grafik pertumbuhan penduduk menunjukkan tren kenaikan yang relatif stabil selama periode 2015–2024. Pada awal periode, jumlah penduduk tercatat sekitar 1,2 juta jiwa dan meningkat secara bertahap hingga mencapai 1,6 juta jiwa pada tahun terakhir. Kenaikan paling signifikan terjadi pada rentang 2018–2020, yang kemungkinan dipengaruhi oleh tingginya angka kelahiran dan arus urbanisasi masuk.
"""
paragraf2 = """
Dari sisi analisis lebih lanjut, rata-rata pertumbuhan per tahun dapat diperkirakan sekitar 3–4%, yang menunjukkan tekanan terhadap kebutuhan infrastruktur, lapangan kerja, serta layanan publik seperti pendidikan dan kesehatan. Jika tren ini berlanjut, pemerintah daerah perlu merencanakan pengembangan wilayah secara berkelanjutan untuk menghindari kepadatan berlebih.
"""
# Ganti <table><tr><td> dengan columns
col1, col2, col3 = st.columns(3)

with col1:
    ""
# st.pyplot(fig)
# st.pyplot(fig2)
    
with col2:
    st.pyplot(fig2)

with col3:
    st.write(paragraf)
    st.write(paragraf2)
#----------------------------

# st.title("Contoh Paragraf di Streamlit")

# ====== Data ======
df_nilai = pd.DataFrame({
    "Nama": ["Andi", "Budi", "Citra"],
    "Nilai": [85, 90, 88]
})

df_penjualan = pd.DataFrame({
    "Produk": ["Cabe", "Gula", "Garam"],
    "Jumlah": [120, 150, 90]
})

# ====== Sidebar Navigation ======
st.sidebar.title("Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["Rumah", "Data Nilai", "Harga Cabai"]
)

# ====== Routing ======
if menu == "Rumah":
    st.title("Dashboard Utama")
    st.write("Silakan pilih menu di sidebar untuk melihat data.")

elif menu == "Data Nilai":
    st.title("Data Nilai Siswa")
    # st.dataframe(df_nilai)
    st.dataframe(
    df_nilai,
    column_config={
        "Nama": st.column_config.TextColumn(
            "Nama Siswa",
            width=100
        ),
        "Nilai": st.column_config.NumberColumn(
            "Nilai",
            width="small"
        ),
    },
    use_container_width=False
)

elif menu == "Harga Cabai":
    st.title("Harga Cabai")
    # st.dataframe(df_penjualan)
    col1_data, col2_data = st.columns([3,7], gap="small")
    with col1_data:
        st.dataframe(
            df_penjualan,
            column_config={
                "Produk": st.column_config.TextColumn(
                    "Nama Produk",
                    width=100
                ),
                "Jumlah": st.column_config.NumberColumn(
                    "Harga",
                    width="small"
                ),
            },
            use_container_width=False
        )
    
    with col2_data:
        st.pyplot(fig)



df_penjualan.head()


