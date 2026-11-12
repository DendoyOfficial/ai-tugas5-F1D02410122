# Tugas 5 Kecerdasan Buatan: Sistem Pakar Sederhana

## 1. Identitas
- Nama: **Moh. Saqif Dendi Al Fayyed**
- NIM: **F1D02410122**

## 2. Topik dan cara menjalankan
**Topik:** kesiapsiagaan banjir dan tanah longsor di tempat tinggal.

- Bahasa: Python 3 (versi 3.8 ke atas), tanpa library tambahan.
- Jalankan: `python main.py` (di folder yang sama dengan `aturan.py`).
- Jawab pertanyaan dengan `y` (ya) atau `t` (tidak).

## 3. Sumber dan tabel aturan

### Sumber
| Kode | Judul | Penerbit | URL | Tanggal akses |
|---|---|---|---|---|
| S1 | Antisipasi Bencana Banjir dan Longsor | BPBD Kabupaten Sumedang (tahun terbit tidak tertera) | https://ppid.sumedangkab.go.id/upload/dokumen/618c82ea8cbad.pdf | 12 November 2026 |
| S2 | Curah Hujan Meningkat, Badan Geologi Ingatkan Potensi Longsor Tinggi dan Kenali Tanda Awalnya (26 Februari 2018) | Kementerian ESDM | https://www.esdm.go.id/id/media-center/arsip-berita/curah-hujan-meningkat-badan-geologi-ingatkan-potensi-longsor-tinggi-dan-kenali-tanda-awalnya- | 12 November 2026 |
| S3 | Mitigasi Bencana Geologi: Gerakan Tanah (materi kuliah tamu oleh penyelidik bumi PVMBG-Badan Geologi) | Teknik Geofisika, Institut Teknologi Sepuluh Nopember (ITS) | https://its.ac.id/tgeofisika/wp-content/uploads/sites/33/2024/10/Materi-Kuliah-Tamu-Teknik-Geofisika-ITS_Mitigasi-Gerakan-Tanah-ITS.pdf | 12 November 2026 |

### Aturan IF-THEN (disimpan di `aturan.py`)
| Aturan | IF | THEN | Sumber |
|---|---|---|---|
| R1 | hujan deras terus-menerus **AND** air sungai/drainase meluap | banjir sedang atau akan terjadi | S1 |
| R2 | tinggal di zona rawan banjir/bantaran sungai **AND** hujan deras terus-menerus | risiko banjir tinggi | S1 |
| R3 | retakan pada tanah/lereng **OR** pohon/tiang/pagar di lereng miring **OR** rembesan air/mata air baru/air keruh di lereng | ada tanda awal gerakan tanah | S2, S3 |
| R4 | tinggal di dekat lereng/tebing **AND** ada tanda awal gerakan tanah **AND** hujan deras terus-menerus | risiko longsor tinggi | S1, S2, S3 |
| R5 | terdengar gemuruh atau sirine peringatan longsor | evakuasi menjauhi arah longsoran | S1 |
| R6 | banjir sedang atau akan terjadi | evakuasi ke tempat yang lebih tinggi | S1 |
| R7 | risiko banjir tinggi **OR** risiko longsor tinggi | siapkan tas siaga dan rute evakuasi | S1 |

Beberapa hasil aturan menjadi syarat aturan lain, sehingga terbentuk rantai inferensi (misalnya R3 → R4 → R7).

## 4. Metode
Metode yang digunakan adalah Forward Chaining (FC). Alasannya karena pengguna biasanya mulai dari kondisi yang ia lihat atau alami, lalu program mencari kesimpulan apa saja yang bisa ditarik. Cocok untuk kesiapsiagaan bencana yang kesimpulannya bertingkat: tanda awal, tingkat risiko, lalu tindakan.

Cara kerja: fakta jawaban "ya" dimasukkan ke memori. Program mengulang: cari aturan yang syaratnya terpenuhi dan hasilnya belum ada di memori, ambil aturan pertama, tambahkan hasilnya ke memori, catat aturan itu sebagai alasan. Berhenti kalau tidak ada aturan baru. Mode `dan` berarti semua syarat harus ada, mode `atau` berarti salah satu cukup.

## 5. Kasus uji
| # | Jawaban "ya" | Kesimpulan yang diharapkan |
|---|---|---|
| 1 | terdengar gemuruh atau sirine peringatan longsor | evakuasi menjauhi arah longsoran |
| 2 | hujan deras terus-menerus saja | **tidak ada** (kasus negatif) |
| 3 | hujan deras terus-menerus, sungai/drainase meluap, tinggal di zona rawan banjir, pohon/tiang miring di lereng, tinggal di dekat lereng | banjir sedang atau akan terjadi, risiko banjir tinggi, ada tanda awal gerakan tanah, risiko longsor tinggi, evakuasi ke tempat yang lebih tinggi, siapkan tas siaga dan rute evakuasi |

Kasus 1 (hanya gemuruh atau sirine = y). Program menjalankan R5 di siklus 1, lalu berhenti di siklus 2. Kesimpulannya evakuasi menjauhi arah longsoran, dengan alasan R5 saja.
![Kasus 1](screenshot/kasus1.png)

Kasus 2 (hanya hujan deras = y). Tidak ada aturan yang cocok karena R1, R2, dan R4 butuh syarat tambahan. Program berhenti di siklus 1 dengan kesimpulan: tidak ada. Ini kasus negatif.
![Kasus 2](screenshot/kasus2.png)

Kasus 3 (hujan, sungai meluap, zona rawan banjir, pohon miring, dekat lereng = y). Program menjalankan R1, R2, R3, R4, R6, dan R7 dalam 6 siklus, lalu berhenti di siklus 7. Ada 6 kesimpulan, antara lain banjir sedang atau akan terjadi, risiko longsor tinggi, dan siapkan tas siaga. Rantai terpanjangnya R3 → R4 → R7: pohon miring jadi tanda gerakan tanah, lalu risiko longsor tinggi, lalu siapkan tas siaga.
![Kasus 3](screenshot/kasus3.png)

## 6. Batas keterbatasan
Pengetahuan dalam sistem ini berasal dari tiga sumber di atas (BPBD Kabupaten Sumedang, Kementerian ESDM/Badan Geologi, dan materi PVMBG di ITS) yang bersifat umum untuk Indonesia, sehingga tidak memakai data lokal seperti peta zona rawan banjir atau gerakan tanah wilayah tertentu, curah hujan real-time, atau kondisi bangunan dan tanah di lokasi pengguna. Hasilnya adalah saran awal untuk membantu bersiap, bukan keputusan akhir; selalu ikuti peringatan resmi BPBD, BMKG, dan Badan Geologi.

## 7. Penggunaan alat bantu AI
Saya memakai Claude Ai untuk membantu mencari sumber dan membantu mengkoreksi kode.  
