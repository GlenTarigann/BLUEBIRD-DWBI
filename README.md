# Bluebird DWBI — Business Analytics

## Deskripsi

Project ini merupakan implementasi **Data Warehouse & Business Intelligence (DWBI)** pada studi kasus Bluebird dengan fokus pada **analisis pola permintaan perjalanan dan optimasi distribusi armada**.

Data yang digunakan merupakan **dataset simulasi (dummy)** untuk keperluan akademik.

Business Analytics dilakukan melalui empat tahap:

1. **Descriptive Analytics** — melihat apa yang terjadi melalui KPI dan pola perjalanan.
2. **Diagnostic Analytics** — menganalisis pola demand berdasarkan kota, jam, dan hubungan antarvariabel.
3. **Predictive Analytics** — memprediksi demand perjalanan menggunakan model yang dibuat pada notebook.
4. **Prescriptive Analytics** — menghasilkan rekomendasi berdasarkan hasil prediksi untuk mendukung distribusi armada.

---

## Struktur Project

```text
BLUEBIRD-DWBI/
│
├── data/
│   └── bluebird_dwbi_dataset.csv
│
├── notebook/
│   └── business_analytics.ipynb
│
├── result/
│   ├── demand_analysis_results.csv
│   └── prediction_recommendation_results.csv
│
├── app.py
├── requirements.txt
└── README.md
```

### Fungsi Folder dan File

| File / Folder      | Fungsi                                                          |
| ------------------ | --------------------------------------------------------------- |
| `data/`            | Menyimpan dataset utama                                         |
| `notebook/`        | Proses Business Analytics dan pembuatan hasil analisis          |
| `result/`          | Menyimpan hasil demand analysis, prediction, dan recommendation |
| `app.py`           | Dashboard Business Analytics menggunakan Streamlit              |
| `requirements.txt` | Daftar library Python yang digunakan                            |
| `README.md`        | Dokumentasi project                                             |

---

## Alur Analisis

```text
Dataset
   ↓
Business Analytics Notebook
   ↓
Descriptive Analytics
   ↓
Diagnostic Analytics
   ↓
Predictive Analytics
   ↓
Prescriptive Analytics
   ↓
Hasil Analisis
   ↓
Streamlit Dashboard
```

Notebook digunakan untuk melakukan proses analisis dan menghasilkan file hasil pada folder `result/`.

`app.py` kemudian membaca dataset dan hasil analisis tersebut untuk menampilkan dashboard.

**Dashboard tidak melakukan training model ulang.**

---

# Dashboard

Dashboard Streamlit menampilkan:

### Descriptive Analytics

* Total Trip
* Revenue
* Average Fare
* Average Rating
* Trip berdasarkan kota
* Trip berdasarkan jam
* Trip berdasarkan service

### Diagnostic Analytics

* Demand berdasarkan kota dan jam
* Correlation matrix

### Predictive Analytics

* Predicted Demand
* Hasil prediksi berdasarkan kota
* Tabel hasil prediction

### Prescriptive Analytics

* Kategori rekomendasi
* Hasil rekomendasi distribusi armada

---

# Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone <URL-REPOSITORY>
```

Masuk ke folder project:

```bash
cd BLUEBIRD-DWBI
```

---

## 2. Buat Virtual Environment

Windows:

```bash
python -m venv .venv
```

Aktifkan:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika berhasil, terminal akan menunjukkan:

```text
(.venv) PS D:\PROJEK GLEN\BLUEBIRD-DWBI>
```

---

## 3. Install Dependencies

Jika tersedia `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Jika belum tersedia, install library secara manual:

```bash
python -m pip install streamlit pandas matplotlib seaborn scikit-learn
```

---

## 4. Jalankan Dashboard

Pastikan terminal berada di folder utama project:

```text
BLUEBIRD-DWBI/
```

Kemudian jalankan:

```bash
python -m streamlit run app.py
```

Streamlit akan menjalankan aplikasi secara lokal.

Biasanya dashboard dapat diakses melalui:

```text
http://localhost:8501
```

---

## 5. Menghentikan Dashboard

Untuk menghentikan aplikasi Streamlit, tekan:

```text
Ctrl + C
```

pada terminal.

---

# Catatan

Dataset yang digunakan merupakan **data simulasi/dummy** untuk kebutuhan akademik. Data tersebut tidak merepresentasikan data internal atau data operasional aktual Bluebird.

Hasil predictive dan prescriptive digunakan sebagai **prototype Business Intelligence** untuk menunjukkan bagaimana data dapat digunakan dalam analisis dan pengambilan keputusan terkait distribusi armada.
