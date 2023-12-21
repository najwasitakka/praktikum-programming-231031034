#Tugas: Komputer mem1ilih angka [1...5]
#       User tebak angka:
#       Jika salah 1: Tebakan salah, anda memiliki 2 kesempatan lagi
#       Jika salah 2: Tebakan salah, anda memiliki 1 kesempatan lagi
#       Jika salah 3: Tebakan salah, belum berhasil
#                     Angka yang dicari adalah x
#       jika benar: Anda Benar angka yang ditebak adalah x (program selesai)


import random

angka = [1,2,3,4,5]

angka_benar = random.choice(angka)

a = True
limit = 3
i = 0

while a:
	i += 1
	pilihan = int(input('Masukan angka secara acak(1-5) : '))

	if pilihan == angka_benar:
		print('Tebakan anda Benar!!')
		print('Angka benar = ',angka_benar)
		a = False
	elif pilihan > len(angka):
		print('Angka harus 1-5 tidak boleh kurang atau lebih!!')
	else:
		if i == limit:
			print('Anda belum berhasil :(')
			a = False
			print('Angka yang di cari adalah ',angka_benar)
		else:
			print(f'Tebakan salah, anda memiliki {limit-i} kesempatan lagi')
			
			
