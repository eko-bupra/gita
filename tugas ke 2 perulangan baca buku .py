"""
Program Perulangan membaca buku
"""
jumlah_buku = 5
print(" ibu berkata, ' baca semua buku ")

jumlah_buku_yang_sudah_dibaca = 0
print(f"jumlah buku yang sudah dibaca{jumlah_buku_yang_sudah_dibaca}")

print(" Dengar for for ")
for jumlah_buku_yang_sudah_dibaca in range (1,jumlah_buku+1):
    print(f"buku ke { jumlah_buku_yang_sudah_dibaca} sudah dibaca ")

print(f"jumlah buku yang sudah dibaca { jumlah_buku_yang_sudah_dibaca}")
print("  ")

# Tanpa for
print(" tanpa for ")
print(" membaca buku ke-1 ")
print(" membaca buku ke-2 ")
print(" membaca buku ke-3 ")
print(" membaca buku ke-4 ")
print(" membaca buku ke-5 ")

