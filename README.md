# Sistem Pakar Diagnosis Penyakit Sapi

[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16-A30000?logo=django)](https://www.django-rest-framework.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-06B6D4?logo=tailwindcss)](https://tailwindcss.com/)
[![Alpine.js](https://img.shields.io/badge/Alpine.js-3.14-8BC0D0?logo=alpinedotjs)](https://alpinejs.dev/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://www.python.org/)

Sistem pakar berbasis web untuk mendiagnosis penyakit pada sapi menggunakan metode **Certainty Factor (CF)**. Dirancang untuk membantu peternak sapi di **Kabupaten Sumbawa, Nusa Tenggara Barat** dalam mengidentifikasi penyakit berdasarkan gejala yang diamati.

## Fitur

- **Diagnosis Penyakit** — Pilih gejala yang dialami sapi, sistem menghitung tingkat kepastian setiap penyakit menggunakan metode CF
- **Basis Pengetahuan** — 11 penyakit dengan 34 gejala dan aturan CF dari literatur veteriner
- **Solusi Penanganan** — Rekomendasi penanganan detail (pengobatan, pencegahan, manajemen, sanitasi, vaksinasi, nutrisi)
- **Riwayat Konsultasi** — Riwayat diagnosis tersimpan per pengguna
- **REST API** — Endpoint JSON untuk integrasi dengan aplikasi lain
- **Admin Panel** — Manajemen data penyakit, gejala, aturan CF, dan solusi via Django Admin

## Daftar Penyakit

| Kode | Penyakit |
|------|----------|
| P01 | Anthrax |
| P02 | Penyakit Mulut dan Kuku (PMK) |
| P03 | Brucellosis |
| P04 | Mastitis |
| P05 | Bloat (Kembung Rumen) |
| P06 | Jembrana Disease |
| P07 | Septikemia Hemoragik (Baliziekte/HS) |
| P08 | Cacingan (Toxocara vitulorum) |
| P09 | Corpus Luteum Persisten |
| P10 | Surra (Trypanosomiasis) |
| P11 | Bovine Ephemeral Fever (Demam 3 Hari) |

## Persyaratan Sistem

- Python 3.11+
- Node.js 18+ (untuk Tailwind CSS CLI)
- SQLite (development) atau PostgreSQL (production)

## Instalasi

### 1. Clone repositori

```sh
git clone <repo-url> sistem-pakar-sapi
cd sistem-pakar-sapi
```

### 2. Virtual environment Python

```sh
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
# source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
npm install
```

### 4. Konfigurasi environment

```sh
# Windows
copy .env.example .env

# Linux / macOS
# cp .env.example .env
```

Edit `.env` sesuai kebutuhan. Untuk development dengan SQLite, nilai default sudah cukup. Untuk production, atur `DEBUG=False`, gunakan `SECRET_KEY` yang kuat, dan konfigurasi koneksi PostgreSQL.

### 5. Migrasi database

```sh
python manage.py migrate
```

### 6. Seed data awal

```sh
python manage.py seed_data           # 5 penyakit + 17 gejala + aturan CF
python manage.py add_new_diseases    # +6 penyakit + 18 gejala + aturan CF
python manage.py seed_solusi         # solusi penanganan komprehensif
```

### 7. Buat admin

```sh
python manage.py createsuperuser
```

### 8. Build Tailwind CSS

```sh
npm run build
```

### 9. Jalankan server

```sh
python manage.py runserver
```

Buka **http://127.0.0.1:8000/** di browser. Daftar akun baru atau login sebagai admin untuk mulai menggunakan sistem.

## Penggunaan

### Web

| URL | Deskripsi |
|-----|-----------|
| `/` | Beranda |
| `/register/` | Daftar akun baru |
| `/login/` | Login |
| `/diagnosa/` | Form diagnosis (pilih gejala) |
| `/hasil/<id>/` | Hasil diagnosis |
| `/riwayat/` | Riwayat konsultasi |
| `/admin/` | Panel administrasi |

### API

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| `GET` | `/api/gejala/` | Daftar semua gejala |
| `POST` | `/api/diagnosa/` | Diagnosis via API |

Contoh request diagnosis via API:

```sh
curl -X POST http://127.0.0.1:8000/api/diagnosa/ \
  -H "Content-Type: application/json" \
  -d '{"gejala_ids": [1, 5, 7]}'
```

## Perintah Penting

```sh
python manage.py runserver              # Jalankan server development
npm run build                           # Build Tailwind CSS (production)
npm run watch                           # Build Tailwind CSS (watch mode)
python manage.py seed_data              # Isi data awal penyakit/gejala/rule
python manage.py add_new_diseases       # Tambah 6 penyakit + gejala baru
python manage.py seed_solusi            # Isi solusi penanganan lengkap
python manage.py check                  # Periksa konfigurasi project
python manage.py createsuperuser        # Buat user admin
python manage.py collectstatic          # Kumpulkan static files (production)
```

## Metode Certainty Factor

Certainty Factor (CF) adalah metode untuk mengukur tingkat kepastian suatu diagnosis berdasarkan gejala yang diamati. Perhitungan dilakukan dengan dua langkah:

1. **CF per gejala**: `CF_gejala = CF_pakar × CF_user` dimana `CF_user = 1.0` (pengguna hanya memilih gejala yang pasti dialami)
2. **Kombinasi CF**: `CF_combined = CF1 + CF2 × (1 − CF1)` diterapkan secara iteratif untuk setiap penyakit

Referensi: Shortliffe & Buchanan (1975).

## Struktur Direktori

```
sistem-pakar-sapi/
├── config/             # Konfigurasi Django
│   ├── settings.py     # Settings (env-based)
│   └── urls.py         # URL root
├── core/               # Aplikasi utama
│   ├── admin.py        # Django Admin
│   ├── cf_engine.py    # Algoritma Certainty Factor
│   ├── models.py       # Model: Penyakit, Gejala, Rule, SolusiPenanganan, NilaiCF
│   ├── views.py        # View berbasis fungsi
│   └── management/     # Management commands (seed data)
├── api/                # REST API (DRF)
│   ├── serializers.py  # DRF serializers
│   ├── urls.py         # API routes
│   └── views.py        # API views
├── templates/          # Django templates
├── static/             # Static files (CSS, JS)
│   ├── css/            # Tailwind input + output + custom CSS
│   └── js/             # Alpine.js
├── manage.py           # Django CLI
├── tailwind.config.js  # Konfigurasi Tailwind CSS
└── package.json        # Node dependencies
```

## Produksi

Untuk deployment production:

1. Set `DEBUG=False` dan `SECRET_KEY` yang kuat di `.env`
2. Konfigurasi PostgreSQL di `.env` (hapus komentar konfigurasi DB)
3. Jalankan `python manage.py collectstatic`
4. Gunakan WSGI server seperti **gunicorn** atau **uvicorn**

## Teknologi

- **Backend**: Django 5.2, Django REST Framework 3.16
- **Frontend**: Tailwind CSS 3.4, Alpine.js 3.14
- **Database**: SQLite (development), PostgreSQL (production)
- **Metode**: Certainty Factor (CF)

## Lisensi

Proyek ini dikembangkan untuk keperluan akademis dan pengabdian masyarakat.
