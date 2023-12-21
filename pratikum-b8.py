# pwd_benar = 'si23'
# a = True
# i = 0
# limit = 3

# while a:
#    i += 1
#    pwd = input('Masukkan Password: ')
#    if pwd == pwd_benar:
#        print('Selamat Anda Login!')
#        a = False
#   else:
#        if i == limit:
#            a = False
#            print('Anda Kehabisan Kesempatan')
#        else:
#            print('Password Salah, Coba Lagi!')


###########################################################3

pwd_benar = 'si23'
a = True
i = 0
limit = 3

while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        print('Password Salah')
        if i == limit:
            a = False
            print('Anda Kehabisan Kesempatan')
        else:
            print(f'Kesempatan Anda Tersisa {limit-i} Kali')


#Tugas: Komputer memilih angka [1...5]
#       User tebak angka:
#       Jika salah 1: Tebakan salah, anda memiliki 2 kesempatan lagi
#       Jika salah 2: Tebakan salah, anda memiliki 3 kesempatan lagi
#       Jika salah 3: Tebakan salah, belum bwehasil
#                     Angka yang dicari adalah x
#       jika benar: Anda Benar angka yang ditebak adalah x (program selesai)
