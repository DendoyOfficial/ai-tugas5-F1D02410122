"""Basis pengetahuan: aturan IF-THEN kesiapsiagaan banjir dan tanah longsor.

Setiap aturan mencatat sumbernya (kode S1-S3 mengacu ke dict SUMBER).
mode "dan"  = semua syarat harus ada di memori
mode "atau" = salah satu syarat cukup
"""

JUDUL = "Kesiapsiagaan banjir dan tanah longsor di tempat tinggal"

BATAS = (
    "Aturan berasal dari 3 sumber (BPBD Kabupaten Sumedang, Kementerian ESDM/Badan Geologi, "
    "dan materi kuliah tamu ITS oleh PVMBG) yang bersifat umum untuk Indonesia. Hasilnya hanya "
    "saran awal, bukan keputusan akhir; selalu ikuti peringatan resmi BPBD, BMKG, dan Badan Geologi."
)

SUMBER = {
    "S1": "Antisipasi Bencana Banjir dan Longsor, BPBD Kabupaten Sumedang, "
          "https://ppid.sumedangkab.go.id/upload/dokumen/618c82ea8cbad.pdf",
    "S2": "Curah Hujan Meningkat, Badan Geologi Ingatkan Potensi Longsor Tinggi dan Kenali Tanda Awalnya, "
          "Kementerian ESDM, https://www.esdm.go.id/id/media-center/arsip-berita/"
          "curah-hujan-meningkat-badan-geologi-ingatkan-potensi-longsor-tinggi-dan-kenali-tanda-awalnya-",
    "S3": "Mitigasi Bencana Geologi: Gerakan Tanah (materi kuliah tamu, PVMBG-Badan Geologi), Teknik Geofisika ITS, "
          "https://its.ac.id/tgeofisika/wp-content/uploads/sites/33/2024/10/"
          "Materi-Kuliah-Tamu-Teknik-Geofisika-ITS_Mitigasi-Gerakan-Tanah-ITS.pdf",
}

ATURAN = [
    {"id": "R1",
     "jika": ["hujan deras turun terus-menerus", "air sungai atau saluran drainase meluap"],
     "mode": "dan",
     "maka": "banjir sedang atau akan terjadi",
     "saran": "Simak informasi banjir resmi dari media dan BPBD.",
     "sumber": ["S1"]},
    {"id": "R2",
     "jika": ["tinggal di zona rawan banjir atau bantaran sungai", "hujan deras turun terus-menerus"],
     "mode": "dan",
     "maka": "risiko banjir tinggi",
     "saran": "Ketahui rute evakuasi dan daerah yang lebih tinggi, serta cara mematikan listrik, air, dan gas.",
     "sumber": ["S1"]},
    {"id": "R3",
     "jika": ["muncul retakan pada tanah atau lereng",
              "pohon, tiang listrik, atau pagar di lereng mulai miring",
              "muncul rembesan air, mata air baru, atau air keruh di lereng"],
     "mode": "atau",
     "maka": "ada tanda awal gerakan tanah",
     "saran": "Waspada dan laporkan tanda tersebut; jangan anggap retakan di lereng sebagai hal biasa.",
     "sumber": ["S2", "S3"]},
    {"id": "R4",
     "jika": ["tinggal di dekat lereng atau tebing", "ada tanda awal gerakan tanah",
              "hujan deras turun terus-menerus"],
     "mode": "dan",
     "maka": "risiko longsor tinggi",
     "saran": "Waspada saat hujan tinggi, jaga drainase agar tidak tersumbat, dan siap mengungsi dari area lereng.",
     "sumber": ["S1", "S2", "S3"]},
    {"id": "R5",
     "jika": ["terdengar gemuruh atau sirine peringatan longsor"],
     "mode": "dan",
     "maka": "evakuasi menjauhi arah longsoran",
     "saran": "Segera evakuasi menjauhi suara gemuruh atau arah datangnya longsoran, menuju zona evakuasi.",
     "sumber": ["S1"]},
    {"id": "R6",
     "jika": ["banjir sedang atau akan terjadi"],
     "mode": "dan",
     "maka": "evakuasi ke tempat yang lebih tinggi",
     "saran": "Segera evakuasi ke tempat yang lebih tinggi; jangan berjalan di arus air atau mengemudi di area banjir.",
     "sumber": ["S1"]},
    {"id": "R7",
     "jika": ["risiko banjir tinggi", "risiko longsor tinggi"],
     "mode": "atau",
     "maka": "siapkan tas siaga dan rute evakuasi",
     "saran": "Siapkan tas siaga bencana, makanan dan air minum untuk minimal tiga hari, "
              "dokumen penting di tempat aman, dan pahami rute evakuasi.",
     "sumber": ["S1"]},
]
