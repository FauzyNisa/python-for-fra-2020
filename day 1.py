# PRINT / TAMPILKAN LAYAR
print("Hello All")  #kalo string dan char pake "" / '
print(1.2)    #kalo int atau float, tinggal tulis

a = 10 #int
b = 3
c = a + b
print ("Hasil %d + %d = %d" % (a,b,c))
print ("Hasil "+str(a)+" + " +str(b)+ " = " +str(c)) # + -> tanda concat. string gabisa di concat dengan int
print("hasil",a,"+",b,"=",c) # , -> 
print(a + b)

# ####################################################################################################################################
# VARIABEL
variabel_string = "isi variabel"
variabel_angka = 1

print(variabel_angka)
print(variabel_string)

# ATURAN PENULISAN VARIABEL
# Nama variabel boleh diawali menggunakan huruf atau garis bawah (_), contoh: nama, _nama, namaKu, nama_variabel.
# Karakter selanjutnya dapat berupa huruf, garis bawah (_) atau angka, contoh: __nama, n2, nilai1.
# (case-sensitif). Artinya huruf besar dan kecil dibedakan. Misalnya, variabel_Ku dan variabel_ku, keduanya adalah variabel yang berbeda.
# Nama variabel tidak boleh menggunakan kata kunci yang sudah ada dalam python seperti if, while, for, dsb.
# huruf besar semua = konstanta C/:NILAI PHI
# huruf besar di awal digunakan untuk Class

# MENGHAPUS VARIABEL
var_a = "saya"
del(var_a)

# print(var_a) #akan eror, karna dah di hapus

# ####################################################################################################################################
# TIPE DATA
# type data -> scalar, tuple, dict
nama = "fauzy"  #string
inisial = "f"   #char (gapaham pas dicek bukan char)
umur = 22       #int
tinggi = 160.5  #float
data_benar = True  #boolean -> True / False

type(nama) #cek nya hiji2 yaaa, tapi gabisa di vs code mah
type(inisial)
type(umur)
type(tinggi)
type(data_benar)

# KONVERSI TIPE DATA
a = 10 #int
b = 3
c = a / b #c itu float 3.33333
print(int(c)) #ngubah si c jadi tipe int -> hasilnya 3
type(c)

# yang bisa -> int(), float(), str(), bool(), < bin(), hex(), oct() > *untuk int

# ####################################################################################################################################
# INPUT OUTPUT

# INPUT
nama = input("Siapa nama kamu: ")
umur = input("Berapa umur kamu: ")

# OUTPUT
print("Hello",nama,"umur kamu adalah",umur,"tahun") #, itu buat gabungin
print("Hello "+nama+" umur kamu adalah "+umur+" tahun") #, itu buat gabungin

# ####################################################################################################################################
# OPERATOR

# ARITMATIKA
# Menggunakan operator penjumlahan
c = a + b
print ("Hasil %d + %d = %d" % (a,b,c))
print ("Hasil "+a+"+" +b+ "=" +c)

# Operator Pengurangan
c = a - b
print ("Hasil %d - %d = %d" % (a,b,c))

# Operator Perkalian
c = a * b
print ("Hasil %d * %d = %d" % (a,b,c))

# Operator Pembagian
c = a / b
print ("Hasil %d / %d = %f" % (a,b,c))

# Operator Sisa pembagian (modulo)
c = a % b
print ("Hasil %d %% %d = %d" % (a,b,c))

# Operator Pangkat
c = a ** b
print ("Hasil %d ** %d = %d" % (a,b,c))

# PENUGASAN, a = 10
# tambahkan dengan 2 -> 10 + 2 = 12
a += 2 

# kurangi 3
a -= 3

# kali 10
a *= 10

# bagi dengan 4
a /= 4

# pangkat 10
a **= 10

# LOGIKA
x = True
y = False
# Logika AND
z = x and y
print ("%r and %r = %r" % (x,y,z))

# Logika OR -> kalo salah satu bener berarti true
z = x or y
print ("%r or %r = %r" % (x,y,z))

# Logika Not
z = not x
print ("not %r  = %r" % (x,z))

# BITWISE , operator berdasarkan nilai biner
# TERNARY, if else dalam 1 baris
# lebih lengkap di https://www.petanikode.com/python-operator/

# PEMBANDING
# apakah a sama dengan b?
c = a == b
print ("Apakah %d == %d: %r" % (a,b,c))

# apakah a < b?
c = a < b
print ("Apakah %d < %d: %r" % (a,b,c))

# apakah a > b?
c = a > b
print ("Apakah %d > %d: %r" % (a,b,c))

# apakah a <= b?
c = a <= b
print ("Apakah %d <= %d: %r" % (a,b,c))

# apakah a >= b?
c = a >= b
print ("Apakah %d >= %d: %r" % (a,b,c))

# apakah a != b?
c = a != b
print ("Apakah %d != %d: %r" % (a,b,c))


