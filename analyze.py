import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
try:
    df = pd.read_csv('reports/PM_Summary_Report.csv')
except FileNotFoundError:
    print("File CSV tidak ditemukan. Pastikan Playbook sudah dijalankan.")
    exit()

# 2. Preprocessing Data
# Gabungkan Tanggal dan Waktu menjadi satu kolom Datetime
df['Timestamp'] = pd.to_datetime(df['Tanggal'] + ' ' + df['Waktu'])

# Bersihkan tanda '%' dan ubah ke tipe data numerik (float)
df['CPU_Usage'] = df['CPU_Status'].str.replace('%', '').astype(float)
df['Mem_Usage'] = df['Memory_Status'].str.replace('%', '').astype(float)

# Urutkan berdasarkan waktu
df = df.sort_values('Timestamp')

# 3. Visualisasi
plt.figure(figsize=(12, 6))

# Plot CPU
plt.plot(df['Timestamp'], df['CPU_Usage'], marker='o', label='CPU Usage (%)', color='tab:red')

# Plot Memory
plt.plot(df['Timestamp'], df['Mem_Usage'], marker='s', label='Memory Usage (%)', color='tab:blue')

# Formatting Grafik
plt.title('Tren Performa Perangkat Network (Health Check)')
plt.xlabel('Waktu Monitoring')
plt.ylabel('Persentase (%)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Simpan sebagai gambar
plt.savefig('reports/Network_Trend_Analysis.png')
print("Grafik berhasil disimpan di reports/Network_Trend_Analysis.png")

# Tampilkan grafik (jika menjalankan di lingkungan GUI)
# plt.show()
