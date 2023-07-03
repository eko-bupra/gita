daftar_buku = (" Seven Habi"," How to Influenser"," frist")
print("tammpilkan Variabel daftar buku")
print( daftar_buku)

print(" \nproses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print(" \ntampilkan isi daftar buku pada index tertentu")
print(daftar_buku[0])
print(daftar_buku[1])
print(daftar_buku[2])

print(" \n tampilkan dengan for in range ")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, "kenji volum 2", -353, 3.54]
print(" \n tampilkan dengan for in range, dimana data tiap elemen berbeda-beda ")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print ("\nkembalikan nilai awal daftar_buku ")
daftar_buku = (" Seven Habi"," How to Influenser"," frist", " 4dx ")
print("\ntambah 1 buku baru ")
daftar_buku  = (" kls 5 ")


for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

