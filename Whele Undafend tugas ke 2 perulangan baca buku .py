"""
Program Perulangan membaca buku dengan while Sampai paham
"""
buku = 10

total_jumlah = 10

print(" ibu berkata, ' baca semua bukumu ")

jumlah_dipahami = 0
print(f"jumlah buku yang sudah dibaca dan dipahami {jumlah_dipahami}")

print(" Dengan while ")
while total_jumlah < buku * 2:
    total_jumlah = total_jumlah + 1
    if jumlah_dipahami == 6:
        print(f"buku ke {jumlah_dipahami + 1} belum paham")
    else:
        jumlah_dipahami = jumlah_dipahami + 1
        print(f" buku ke {jumlah_dipahami} sudah dibaca dan dipahami ")

print(f"jumalh buku yang sudah dibaca dan dipahami {jumlah_dipahami}")
if jumlah_dipahami == buku :
    print (" bu, semua buku  sudah dibaca dan dipahami ")
else :
    print (f" bu, tidak semua buku bisa dipahami."
           f" budi hanya bisa memahami {jumlah_dipahami} buku ")
