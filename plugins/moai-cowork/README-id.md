<div align="center">

# 🗿 MoAI-Cowork

**100 Harness Domain Berkembang Sendiri — Ahli AI Pribadi Anda**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## Apa itu MoAI?

**MoAI-Cowork** adalah plugin untuk Claude Cowork yang menyediakan 100 harness pakar domain melalui sistem asisten AI yang belajar sendiri.

Sebuah harness adalah modul pakar AI yang menggabungkan pengetahuan khusus domain, alur kerja, format deliverable, dan protokol pengumpulan konteks ke dalam satu paket. Setelah dipasang, MoAI bertransformasi menjadi pakar domain dan memberikan hasil terstruktur.

**Fitur utama:**

- 10 kategori × 100 harness — konten, pemasaran, bisnis, pendidikan, hukum, gaya hidup, komunikasi, operasi, keuangan, dan produk/inovasi
- Arsitektur pembelajaran mandiri 5 lapisan — berkembang dan beradaptasi dengan pengguna seiring waktu
- Profil global — bagikan informasi pribadi + perusahaan di seluruh sesi, tidak perlu memasukkan ulang
- Dukungan 17 bahasa — sumber tunggal EN + lokalisasi runtime
- Dukungan lokal di seluruh dunia — masukkan negara kerja Anda dan MoAI secara otomatis mengumpulkan hukum pajak, hukum ketenagakerjaan, perlindungan data, dan praktik bisnis melalui pencarian web

---

## Instalasi

### Metode 1: Instal dari Claude Cowork Marketplace (Direkomendasikan)

1. Luncurkan aplikasi **Claude Desktop**
2. Masuk mode **Cowork** dari kiri bawah
3. Klik ikon **Plugin (🧩)** di samping input chat
4. Cari `moai-cowork` di marketplace
5. Temukan **MoAI-Cowork** dan klik **Install**
6. Setelah instalasi, ketik `/moai init` dalam chat untuk memulai pengaturan awal

### Metode 2: Instal dari K-Harness Marketplace

K-Harness adalah marketplace yang menyertakan MoAI-Cowork.

```
# Langkah 1: Tambahkan marketplace
/plugin marketplace add modu-ai/k-harness

# Langkah 2: Instal plugin MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### Metode 3: Instal Langsung dari GitHub

```
# Kloning repository
git clone https://github.com/modu-ai/k-harness.git

# Navigasi ke direktori plugin
cd k-harness/plugins/moai-cowork

# Muat secara manual di Claude Desktop
# Cowork mode → Plugin (🧩) → "Install from file" → pilih folder moai-cowork
```

### Metode 4: Instal Manual via ZIP

1. Unduh `moai-cowork-v0.1.3.zip` terbaru dari halaman [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. Buka Claude Desktop → masuk mode Cowork
3. Klik ikon Plugin (🧩) → **Install from file**
4. Pilih file ZIP yang telah diunduh

---

## Pembaruan

### Jika diinstal melalui marketplace

```
# Perbarui marketplace K-Harness
/plugin marketplace update k-harness

# Atau melalui UI Cowork:
# Plugin (🧩) → MoAI-Cowork → klik "Update"
```

### Jika diinstal dari GitHub

```
cd k-harness
git pull origin main
```

### Jika diinstal melalui ZIP

1. Hapus plugin yang ada: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Unduh file ZIP terbaru
3. Ulangi proses instalasi manual Metode 4

### Periksa versi

Ketik `/moai status` dalam chat untuk memverifikasi versi yang saat ini dipasang.

---

## Pemecahan Masalah

### Plugin tidak dikenali

1. Keluar sepenuhnya dan mulai ulang Claude Desktop
2. Periksa apakah MoAI-Cowork muncul dalam daftar Plugin (🧩) di mode Cowork
3. Jika tidak, coba pasang kembali

### Kesalahan pada `/moai init`

1. Ketik `/moai doctor` untuk menjalankan diagnostik lingkungan
2. Jika profil global Anda rusak, atur ulang dengan `/moai profile --reset`

### Harness tidak memuat

1. Periksa apakah `.moai/config.json` ada di folder proyek Anda
2. Jika tidak, inisialisasi kembali dengan `/moai init`

### Data lokalisasi tidak dikumpulkan

- Korea: Menggunakan data bawaan (tidak perlu pencarian web)
- Negara lain: Memerlukan koneksi internet dan alat pencarian web

---

## Memulai dengan Cepat

### Langkah 1: Inisialisasi

```
/moai init
```

MoAI melakukan wawancara interaktif untuk mengumpulkan profil Anda (nama, peran, perusahaan, lokal).

### Langkah 2: Jelajahi Katalog Harness

```
/moai catalog
```

Lihat daftar lengkap 100 harness di 10 kategori.

### Langkah 3: Buat Permintaan Bahasa Alami

```
Bantu saya melakukan riset pasar
```

MoAI secara otomatis mendeteksi harness `market-research` dan berjalan dalam mode ahli.

---

## Katalog 100 Harness

| # | Kategori | Jumlah | Contoh Harness |
|---|----------|--------|-----------------|
| 1 | Konten & Kreatif | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Bisnis & Strategi | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Pemasaran & Pertumbuhan | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Pendidikan & Penelitian | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Hukum & Kepatuhan | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Gaya Hidup | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Komunikasi & Dokumen | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Operasi & HR | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Keuangan & Perdagangan | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Produk & Inovasi | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Lihat daftar lengkap 100 harness dengan `/moai catalog`.

---

## Perintah Kunci

| Perintah | Deskripsi |
|---------|-------------|
| `/moai init` | Inisialisasi — kumpulkan profil dan instal harness |
| `/moai catalog` | Jelajahi katalog 100 harness |
| `/moai status` | Periksa harness yang dipasang dan status evolusi |
| `/moai evolve` | Jalankan siklus evolusi pembelajaran mandiri |
| `/moai profile` | Lihat/edit profil global |
| `/moai doctor` | Jalankan diagnostik lingkungan |
| `/moai help` | Tampilkan perintah yang tersedia |

---

## Arsitektur

```
Layer 0: auto-memory (global) — profil pengguna, riwayat harness
Layer 1: plugin (read-only) — 100 harness dasar (sumber tunggal en/, lokalisasi runtime)
Layer 2: .claude/CLAUDE.md + rules/ — persona
Layer 3: .moai/ (read/write) — konteks domain, data evolusi
Layer 4: auto-memory learning — akumulasi umpan balik lintas sesi
```

---

## Lisensi

MIT License — bebas digunakan, dimodifikasi, dan didistribusikan

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Suggestions**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Temui Pakar AI Anda.**

*Version 0.1.3 | Last Updated: 2026-04-08*
