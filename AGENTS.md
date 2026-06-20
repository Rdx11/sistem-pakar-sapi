# AGENTS.md — Sistem Pakar Penyakit Sapi

## Stack
- Django 5.2 + DRF 3.16 / Tailwind CSS 3.4 (CLI, standalone) / Alpine.js 3.14
- Python 3.11, SQLite (dev) / PostgreSQL (prod)
- All JS is plain inline Alpine; no bundler, no SPA.

## Commands
```sh
python manage.py migrate
python manage.py seed_data           # 5 diseases + 17 symptoms + CF rules
python manage.py add_new_diseases    # +6 diseases + 18 more symptoms + rules
python manage.py seed_solusi         # comprehensive solutions for all diseases
python manage.py createsuperuser

npm run build    # tailwindcss -i static/css/input.css -o static/css/main.css --minify
npm run watch    # rebuild on changes
```

## Architecture
- **`config/`** — Django project settings (language `id`, tz `Asia/Makassar`)
- **`core/`** — main app: models, function-based views, admin, CF engine
- **`api/`** — REST app (DRF): `GET /api/gejala/` + `POST /api/diagnosa/`
- **`core/cf_engine.py`** — `hitung_cf(gejala_ids)` implements Certainty Factor: CF = CF_pakar × CF_user (1.0), combined iteratively as `CF1 + CF2×(1−CF1)`
- **Templates** at `templates/`, static at `static/` — no build step beyond Tailwind

## Models
- `Penyakit` (kode P01-P11), `Gejala` (kode G01-G34), `Rule` (disease↔symptom CF link)
- `SolusiPenanganan` — per-disease solutions with `jenis` enum (pengobatan/pencegahan/manajemen/sanitasi/vaksinasi/nutrisi)
- `NilaiCF` — consultation history with JSON fields `gejala_dipilih` + `hasil_cf`

## Testing
No test suite in the repo.

## Routes
| Path | View | Auth |
|------|------|------|
| `/` | home | public |
| `/login/` `/register/` `/logout/` | auth | public |
| `/diagnosa/` `POST` | CF calculation | login_required |
| `/hasil/<pk>/` | result detail | login_required |
| `/riwayat/` | history (filtered by user) | login_required |
| `/admin/` | Django admin | staff |
| `GET /api/gejala/` | symptom list | none (AllowAny) |
| `POST /api/diagnosa/` | CF via API | none (AllowAny) |

## Important
- `.env` is required (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` — see `.env.example`)
- DB switch to PostgreSQL by setting `DB_ENGINE` in `.env`
- DRF has no auth configured — `AllowAny`, `JSONRenderer` only
- Django messages are the flash notification system — CSS classes: `error`/red, `warning`/yellow, else blue
- Diagnosa requires selecting ≥1 symptom; each symptom gets CF_user=1.0
- Riwayat scoped by user name: staff/superuser sees all, others filtered by `nama_pemilik__icontains`
