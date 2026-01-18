# 📶 WiFi / Network Device Monitor
Kunjungi : [PasteLkun](https://pastelkun.com/wifi-monitor-cara-gampang-scan-device-di-jaringan-lu/)

<img width="1875" height="933" alt="Opera Snapshot_2026-01-18_080915_localhost" src="https://github.com/user-attachments/assets/90b83cd6-15b8-45a4-963b-b67819c1043d" />

Aplikasi ini adalah **network scanner berbasis Python** yang digunakan untuk **menampilkan daftar device (HP, laptop, TV, IoT, dll)** yang sedang **aktif dan terhubung ke jaringan LAN atau WiFi**.

Aplikasi **tidak melakukan penyadapan traffic**, tidak membaca website, dan **aman digunakan** untuk kebutuhan monitoring jaringan rumahan atau kantor kecil.

---

## ✨ Fitur Utama

- 🔍 Scan device aktif di jaringan lokal
- 🖥️ Menampilkan:
  - IP Address
  - MAC Address
  - Hostname (jika tersedia)
  - Status device
  - Waktu terakhir terdeteksi
- 🌐 Bisa mendeteksi device **LAN & WiFi**
- 🧭 Tampilan web (via browser)
- 🔄 Scan ulang kapan saja

---

## 🛠️ Teknologi yang Digunakan

- **Python 3** – bahasa utama
- **Streamlit** – web interface
- **Nmap** – engine network scanning
- **python-nmap** – integrasi Nmap dengan Python
- **Pandas** – pengolahan data

---

## ⚙️ Cara Kerja Singkat

1. User memasukkan **network range** (contoh: `192.168.1.0/24`)
2. Klik tombol **Scan Devices**
3. Aplikasi menjalankan perintah Nmap (`-sn` ping scan)
4. Device yang aktif akan merespon
5. Data ditampilkan dalam tabel di browser

---

## 📦 Persyaratan Sistem

- OS:
  - ✅ Windows 10 / 11
  - Linux / macOS juga didukung
- Koneksi jaringan:
  - LAN (kabel) atau WiFi

---

## 🚀 Instalasi di Windows 10

### 1️⃣ Install Python

- Download Python dari website resmi
- Saat instalasi **WAJIB centang**:
  - ✅ `Add Python to PATH`

Cek instalasi:
```bash
python --version
```

---

### 2️⃣ Install Nmap (WAJIB)

- Download Nmap for Windows dari website resmi Nmap
- Install seperti biasa

Cek apakah Nmap sudah terpasang:
```bash
nmap -V
```

> ⚠️ Pastikan `nmap` bisa dipanggil dari Command Prompt (PATH sudah benar)

---

### 3️⃣ Install Library Python

Buka Command Prompt / PowerShell:
```bash
pip install streamlit python-nmap pandas
```

---

### 4️⃣ Jalankan Aplikasi

Masuk ke folder project, lalu jalankan:
```bash
streamlit run app.py
```

Browser akan otomatis terbuka di:
```
http://localhost:8501
```

---

## 🧪 Cara Menggunakan

1. Masukkan **Network Range**
   - Contoh umum:
     - `192.168.1.0/24`
     - `192.168.0.0/24`

2. Klik **Scan Devices**
3. Lihat daftar device yang terhubung
4. Scan ulang jika diperlukan

---

## 🔐 Keamanan & Privasi

Aplikasi ini:
- ❌ Tidak menyadap traffic
- ❌ Tidak membaca HTTPS
- ❌ Tidak memonitor aktivitas browsing
- ❌ Tidak memerlukan password WiFi

Aplikasi **hanya melakukan identifikasi device jaringan** menggunakan metode standar Nmap.

---

## ⚠️ Keterbatasan

- Device yang sleep / idle bisa tidak terdeteksi
- Beberapa router menyembunyikan MAC Address
- Hostname sering kosong
- Scan bersifat **snapshot**, bukan real-time monitoring

---

## 👥 Cocok Digunakan Untuk

- Monitoring WiFi rumah
- Admin kos / kantor kecil
- Edukasi jaringan komputer
- Audit device jaringan sederhana

---

## 📈 Rencana Pengembangan (Opsional)

- Deteksi device baru
- Label manual device
- Auto scan berkala
- Export ke CSV
- Sistem login

---

## 📄 Lisensi

Bebas digunakan untuk keperluan pribadi dan edukasi.

---

> Dibuat untuk pembelajaran dan monitoring jaringan lokal secara aman.

