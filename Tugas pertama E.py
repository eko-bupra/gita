# TUGAS PERTAMA
print (" mulai ")
print (" ibu memberi perintah beli 1 botol susu ' ? ")
print (" anak : Anak Menjawab ' OK ' ")
print (" anak pergi ketoko ")
print (" anak : anak mengecek tidak ada susu ditoko ")
print (" ibu  : bertanya kembali apakah diwarung ada 6 butir telur  ")
print (" anak menjawab ada  ")
print (" ibu  : belikan 6 butir teluar aja untuk susunya di censel aja  ")
print (" Anak Pulang Ke rumah  ")
print (" Menyerahkan Hasil Belanja Kepada Ibu ")
print (" Selesai  ")

# Percabangan
jumlah_botol_susu = 6
jumlah_telur = 1
print (f"jumlah botol susu {jumlah_botol_susu} btl")
print (f"jumlah Telur {jumlah_telur} btl")

if jumlah_botol_susu > 0:
    print (" budi mengecek harganya, dan ternyata uangnya cukup ")
    if jumlah_telur == 0:
        print (" Budi Membeli 1 botol susu ")
    else:
        print (" budi membeli 6 botol susu ")
else:
    print (" budi tidak jadi memebeli 1 botol susu ")
