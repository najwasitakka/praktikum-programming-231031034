print('Tugas Praktikum 4'.center(35))
nama = 'Najwa Sitakka'
nim  = '231031034'
prodi= 'Sistem Informasi B'

print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''

print()
str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON
print("str1 =",str1)
a = str1.upper()           #membuat string menjadi huruf besar
b = a.strip("NEUMANN")     #menghilangkan kata NEUMAN dalam string
c = "NEUMANN " + b.upper() #menambahkan kata neuman yang hilang tadi ke awalan string
print("output =",c)

print()
str2 = 'duFort Frankel Von Neumann'
print("str2 =",str2)
#output: dfv neumann
a = str2.lower() #membuat string menjadi lowercase/huruf kecil
b = a[19:]       #menampilkan index string ke 19 sampai akhir
c = "dfv " + b   #menambahkan kata "dfv" ke string
print("output =",c) #cara mudah (dikit)

print()
str3 = 'duFort Frankel Von Neumann'
print("str3 =",str3)
#output: DUFORT F V N
a = str3.upper() #membuat string menjadi uppercase/huruf besar
b = a[0:6] #menampilkan index 0 sampai 6
c = a[7]   #menampilkan index 7
d = a[15]  #menampilkan index 5
e = a[19]  #menampilkan index 19, cara susah
print("output =",b,c,d,e) #menampilkan semua variabel yg berisi index string

print()
str4 = 'duFOrt Frankel Von Neumann'
print("str4 =",str4)
#output: N duFort f v
a = str4.title()       #mengubah string jadi huruf kecil
b = a.replace("D","d") 
c = b.replace("f","F") # variabel a dan b merubah output menjadi "duFort Frankel Von Neumann"
d = b.lower()    # mengubah variabel b menjadi lowercase
e = a[19]     # mengambil index ke 19 dari variabel a = "N"
f = c[0:6]    # menagambil index dari 0 sampai 6 variabel c = "duFort"
g = d[7]      # mengambil index ke 7 dari variabel d = "f"
h = d[15]     # mengambil index ke 15 dari variabel d = "v"
print("output =",e,f,g,h) #Cara paling susah, menyusahkan dan susah dimengerti

print()
str5 = 'DuFort Frankel Von Neumann'
print("str5 =",str5)
#output: NEUMANN d f v
a = str5.replace(str5,"Neumann") #Hanya menyisakan kata "Neumann"
b = str5.lower() #mengubah variabel str5 menjadi lowercase/huruf kecil
c = a.upper() #mengubah variabel a = "Neumann" menjadi uppercase/huruf besar
d = b[0]   #mengambil index ke 0 dari variabel b 
e = b[7]   #mengambil index ke 7 dari variabel b
f = b[15]  #mengambil index ke 15 dari variabel b
print("output =",c,d,e,f)

print()
str6 = 'duFort Frankel Von Neumann'
print("str6 =",str1)
#output: NEUMANN DFV
a = str5.replace(str5,"Neumann") #Hanya menyisakan kata "Neumann"
b = str5.upper() #mengubah variabel str5 menjadi uppercase/huruf besar
c = a.upper() #mengubah variabel a = "Neumann" menjadi uppercase/huruf besar
d = b[0]   #mengambil index ke 0 dari variabel b 
e = b[7]   #mengambil index ke 7 dari variabel b
f = b[15]  #mengambil index ke 15 dari variabel b
print("output =",c,d+e+f)

print()
str7 = '@duFort Frankel Von Neumann$'
print("str7 =",str7)
#output: duFort Frankel Von NEUMANN
a = str7.strip("@$") #Menghilangkan tanda baca
b = a.strip("Neumann") #Menghilangkan kata "Neumann" dalam variabel a
c = str7.replace(str7,"Neumann") #Menyisakan kata "Neumann" dalam variabel str7
d = c.upper() #mengubah variabel c = "Neumann" dangan upppercase 
print("output =",b+d) #menampilkan var b dan d  

print()
str8 = '#duFort@Frankel@Von@Neumann$'
print("str8 =",str8)
#output: duFort Frankel Von Neumann
a = str8.strip("#$") #menghapus tanda # dan $
b = a.replace("@"," ") #Mengganti tanda @ dengan spasi
print("output =",b)

print()
str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
print("str9 =",str9)
#output: duFort Frankel Von Neumann
a = str9.strip("@$") #menghapus tanda paling kanan dan kiri
b = a.replace("@#^", " ") #mengubah tanda yg memisahkan kalimat 1 dan 2 menjadi spasi
c = b.replace("*#(", " ") #mengubah tanda yg memisahkan kalimat 2 dan 3 menjadi spasi
d = c.replace("(#(", " ") #mengubah tanda yg memisahkan kalimat 3 dan 4 menjadi spasi
print("output",d) 

print()
str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
print("str10 =",str10)
#output: duFort Frankel Von Neumann
a = str10.strip("@^") #menghapus tanda paling kiri dan kanan
b = a.replace("@!^"," ") #mengubah tanda yg memisahkan kalimat 1 dan 2 menjadi spasi
c = b.replace("!1("," ") #mengubah tanda yg memisahkan kalimat 2 dan 3 menjadi spasi
d = c.replace("(!("," ") #mengubah tanda yg memisahkan kalimat 3 dan 4 menjadi spasi
e = d.title()            #mengubah variabel d menjadi title atau semua kalimat diawali dengan uppercase
f = e.replace("D","d")   #Mengubah kata D menjadi d
g = f.replace("f","F")   #mengubah kata f menjadi F
print("output =",g)
