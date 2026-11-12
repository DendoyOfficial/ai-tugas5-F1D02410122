"""Sistem pakar sederhana: kesiapsiagaan banjir dan longsor (Forward Chaining).

Cara jalan:  python main.py   (aturan dibaca dari aturan.py)
"""
from aturan import JUDUL, BATAS, SUMBER, ATURAN


def daftar_fakta_dasar(kb):
    """Fakta yang ditanyakan ke user = syarat yang bukan hasil aturan mana pun."""
    hasil_aturan = {r["maka"] for r in kb["aturan"]}
    fakta = []
    for r in kb["aturan"]:
        for syarat in r["jika"]:
            if syarat not in hasil_aturan and syarat not in fakta:
                fakta.append(syarat)
    return fakta


def tanya_user(fakta_dasar):
    jawaban = []
    print("Jawab y/t.")
    for i, f in enumerate(fakta_dasar, 1):
        while True:
            j = input(f"{i}. Apakah {f}? (y/t) > ").strip().lower()
            if j in ("y", "t"):
                break
            print("   Ketik y atau t saja.")
        if j == "y":
            jawaban.append(f)
    return jawaban


def syarat_terpenuhi(aturan, memori):
    cek = all if aturan["mode"] == "dan" else any
    return cek(s in memori for s in aturan["jika"])


def forward_chaining(kb, fakta_awal):
    memori = set(fakta_awal)
    alasan = {}  # hasil -> aturan yang menghasilkannya
    log = []
    siklus = 0
    while True:
        siklus += 1
        cocok = [r for r in kb["aturan"]
                 if syarat_terpenuhi(r, memori) and r["maka"] not in memori]
        if not cocok:
            log.append(f"Siklus {siklus}: tidak ada aturan baru, berhenti")
            break
        r = cocok[0]  # ambil aturan pertama
        memori.add(r["maka"])
        alasan[r["maka"]] = r
        log.append(f"Siklus {siklus}: {r['id']} -> {r['maka']}")
    return memori, alasan, log


def cetak_alasan(fakta, alasan, memori, tingkat=0):
    r = alasan.get(fakta)
    if r is None:
        return
    dipakai = [s for s in r["jika"] if s in memori]
    sambung = " DAN " if r["mode"] == "dan" else " ATAU "
    print("  " * (tingkat + 1) + f"{fakta}  <- {r['id']} ({sambung.join(dipakai)})  [{', '.join(r['sumber'])}]")
    for s in dipakai:
        cetak_alasan(s, alasan, memori, tingkat + 1)


def main():
    kb = {"judul": JUDUL, "batas": BATAS, "sumber": SUMBER, "aturan": ATURAN}
    print(kb["judul"])

    fakta_awal = tanya_user(daftar_fakta_dasar(kb))
    print("\nFakta awal:", ", ".join(fakta_awal) if fakta_awal else "(tidak ada)")
    print()

    memori, alasan, log = forward_chaining(kb, fakta_awal)
    for baris in log:
        print(baris)

    print()
    if not alasan:
        print("Kesimpulan: tidak ada kesimpulan yang dapat ditarik dari fakta tersebut.")
    else:
        print("Kesimpulan:", ", ".join(alasan))
        print("Alasan:")
        # tampilkan alasan untuk hasil yang bukan bahan aturan lain (kesimpulan akhir)
        dipakai_aturan_lain = {s for r in alasan.values() for s in r["jika"]}
        for k in alasan:
            if k not in dipakai_aturan_lain:
                cetak_alasan(k, alasan, memori)
        print("Saran:")
        for k, r in alasan.items():
            print(f"  - {k}: {r['saran']}")

    print("\nSumber:")
    for kode, ket in kb["sumber"].items():
        print(f"  {kode}: {ket}")
    print("\nCatatan:", kb["batas"])


if __name__ == "__main__":
    main()
