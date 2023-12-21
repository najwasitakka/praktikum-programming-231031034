print('pratikum-3 \n\n')
print('Nama  : Najwa Sitakka')
print('NIM   : 231031034')
print('Prodi : Sistem Informasi B')

####################################
a = True
b = False

print('\n============NAND============')
hasil = not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil = not (a and b)
print(a,'nand',b,'adalah =',hasil)
hasil = not (b and a)
print(b,'nand',a,'adalah =',hasil)
hasil = not (b and b)
print(b,'nand',b,'adalah =',hasil)

print('\n============NOR============')
hasil = not (a or a)
print(a,'nor',a,'adalah =',hasil)
hasil = not (a or b)
print(a,'nor',b,'adalah =',hasil)
hasil = not (b or a)
print(b,'nor',a,'adalah =',hasil)
hasil = not (b or b)
print(b,'nor',b,'adalah =',hasil)

print('\n============NXOR============')
hasil = not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil = not (a ^ b)
print(a,'nxor',b,'adalah =',hasil)
hasil = not (b ^ a)
print(b,'nxor',a,'adalah =',hasil)
hasil = not (b ^ b)
print(b,'nxor',b,'adalah =',hasil)

# INI OPERATOR MEMBERSHIP
print('\n============ IN ============')
nama = 'Najwa Sitakka'

test = 'wa' #ISI DENGAN 2 HURUF ADA DI NAMA
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

test = 'ta' #ISI DENGAN 2 HURUF ADA DI NAMA
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

print()
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print (test1,'ada di',nama,'adalah=',cek)

cek = test2 in nama
print (test2,'ada di',nama,'adalah=',cek)

cek = test3 in nama
print (test3,'ada di',nama,'adalah=',cek)

cek = test4 in nama
print (test4,'ada di',nama,'adalah=',cek)

cek = test5 in nama
print (test5,'ada di',nama,'adalah=',cek)
#TUGAS lanjutkan kode
#dengan cara yang sama buat operator not in

# INI Operator BITWISE
print('\n')
a = 27 #tanggal lahir
b = 2 #bulan lahir
a += 60
b -= 80
print('========AND========')
print('Nilai',a,'biner adalah      =',format(a,'08b'))
print('Nilai',b,'biner adalah     =',format(b,'08b'))
print('---------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah=',format(c,'08b'))

print ('\n============OR============')
#Tugas untuk OR

print ('\n============XOR============')
#Tugas untuk XOR

print ('\n============NOT============')
c = ~a
print('Nilai',a,'biner adalah     =',format(a,'09b'))
print('Nilai not',a,'biner adalah =',format(c,'09b'))
#Tugas Lanjutan untuk not b

print('\n============Left Shift============')
c = a << 2
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',a,'<< 2 biner adalah =',format(c,'09b'))
c = b << 2
print('Nilai',b,'biner adalah     =',format(b,'09b'))
print('Nilai',b,'<< 2 biner adalah=',format(c,'09b'))

print('\n============Right Shift============')
c = a >> 2
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',a,'>> 2 biner adalah =',format(c,'09b'))
c = b >> 2
print('Nilai',b,'biner adalah     =',format(b,'09b'))
print('Nilai',b,'>> 2 biner adalah=',format(c,'09b'))

print('\n============NOT AND============')
#Tugas buat untuk NAND
print('\n============NOT OR============')
#Tugas buat untuk NOR
print('\n============NOT XOR============')
#Tugas buat untuk NXOR
print('\n============NOT << 2============')
#Tugas buat untuk c = ~(a<<2)
#Tugas buat untuk c = ~(b<<2)
print('\n============NOT >> 2============')
#Tugas buat untuk c = ~(a>>2)
#Tugas buat untuk c = ~(b>>2)











