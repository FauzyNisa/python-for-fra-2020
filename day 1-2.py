# ####################################################################################################################################
# PERCABANGAN
# IF
nama = "budi"

if nama == "budi":
   print("Kamu adalah budi")

# IF ELSE
if nama != "budi":
   print("Kamu bukan budi")
else:
    print("Kamu adalah budi")

# ELIF
nilai = -2
if nilai >= 80:
   print("Grade A")
elif nilai >= 50:
    print("Grade B")
elif nilai >= 0:
    print("Grade C")
else:
    print("Maaf nilai tidak terdeteksi")

# ####################################################################################################################################
# PERULANGAN
# FOR, wajib ada range / batasan
ulang = 10

for i in range(ulang):
    i+=1
    print ("Perulangan ke-"+str(i))

# WHILE, suka2 mo ada atau ga pun terserah
jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")

print ("Total perulagan: " + str(hitung))

# ####################################################################################################################################
# STRUKTUT DATA LIST
# List kosong
warna = []

# Membuat list dengan isi 1++ item
hobi = ["membaca", "menulis", "bermain"]

# Membuat list dengan isi macam2
wadah = ["buku", 21, True, 34.12]

# TAMPILKAN LIST
print (hobi[1]) #dengan urutan
print (hobi) #semua
len(wadah) #panjang atau banyak isi

for isi in wadah:
    print(isi)

# GANTI NILAI LIST, mutable
# mengubah nilai index ke-2
hobi[2] = "mendengarkan musik"
print(hobi)

# MENAMBAH ISI LIST
# Append (belakang)
hobi.append("makan")
print(hobi)

# Insert (menambahkan dimanapun)
hobi.insert(0,"minum")
print(hobi)

# Sort (mengurutkan)
print(sorted(hobi))

angka =[1,3,5,0,2,7]
print(sorted(angka,reverse=True)) #kebalikan

# MENGHAPUS ISI LIST
del(hobi[0]) #urutan
print(hobi)

# MEMOTONG
# potong index 0, index 3 dst
print (angka[1:3])

# OPERASI LIST
print(angka + hobi) #penjumlahan
print(angka * 5) #perkalian

# 2 DIMENSI
minuman = [
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es Kopi", "Es Campur", "Es Teler"]
]
print(minuman[2][1]) #minuman[baris][kolom]

# ####################################################################################################################################
# STRUKTUT TUPLE, gabisa diubah isinya, immutable
laci = (1234, 432, 'World!') #bisa juga gapake kurung
print(laci)

# AKSES NILAI TUPLE
print(laci[1])

# MOTONG TUPLE
print(laci[1:2])

# TUPLE NESTED
lemari = ("hello", 1999, 46.2)
ruangan = (laci, lemari)
print(ruangan)

# SEQUENCE UNPACKING, diextract
kata, tahun, berat = lemari
print(kata) #jadi variabel
print(tahun)
print(berat)

# ####################################################################################################################################
# STRUKTUT DATA DICT
nama_dict = {
    "key": "value"
}

mahasiswa = {
    "nama": "Budi",
    "umur": 22,
    "hobi": ["coding", "membaca", "bernyanyi"],
    "menikah": False,
    "sosmed": {
        "facebook": "budi",
        "twitter": "@budi"
    } 
}

# MENGAKSES ISI DICT
print("Nama saya adalah " + mahasiswa["nama"])
print("Twitter: " + mahasiswa["sosmed"]["twitter"])

print(mahasiswa["hobi"])

print(mahasiswa.get("umur"))

# PERULANGAN
for value in mahasiswa:
    print(mahasiswa[value])

for key, val in mahasiswa.items():
    print("%s : %s" % (key, val))

# MENGUBAH ISI DICT
mahasiswa["nama"] = "Hana"
print(mahasiswa["nama"])

# MENGHAPUS
del(mahasiswa["hobi"])
print(mahasiswa)

# MENAMBAHKAN ITEM
mahasiswa.update({"pekerjaan":"asisten lab"})
print(mahasiswa)