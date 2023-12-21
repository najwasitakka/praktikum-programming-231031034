#print('Hallo')

##judul
#print('Program Menghitung Volume dan Luas Permukaan Balok'.center(45))
#print('Bangun Ruang Balok'.center(45))
#print()

##inputan
#p = float(input('Masukkan Panjang: '))
#l = float(input('Masukkan Lebar: '))
#t = float(input('Masukkan Tinggi: '))

##hitung
#vol = p*l*t
#luas_surf = 2*(p*l + p*t + l*t)
#luas_non_tutup = luas_surf - p*l

##tampilan
#print(f'Hasil perhitungan Volume : {vol}')
#print(f'Hasil perhitungan Luas Permukaan : {luas_surf}')
#print(f'Hasil perhitungan Luas Permukaan tanpa tutup : {luas_non_tutup}')


######################################################################################

#a = True

#while a:
#    print('Hallo')
    
#    #judul
#    print('Program Menghitung Volume dan Luas Permukaan Balok'.center(45))
#    print('Bangun Ruang Balok'.center(45))
#    print()

#    #inputan
#    p = float(input('Masukkan Panjang: '))
#    l = float(input('Masukkan Lebar: '))
#    t = float(input('Masukkan Tinggi: '))

#    #hitung
#    vol = p*l*t
#    luas_surf = 2*(p*l + p*t + l*t)
#    luas_non_tutup = luas_surf - p*l

#    #tampilan
#    print(f'Hasil perhitungan Volume : {vol}')
#    print(f'Hasil perhitungan Luas Permukaan : {luas_surf}')
#    print(f'Hasil perhitungan Luas Permukaan tanpa tutup : {luas_non_tutup}')

#    #pilihan
#    pilih = input('Apakah lanjutkan? [y/n]')
#    if pilih == 'y':
#        a = True
#    else:
#        a = False
#        print('Terima Kasih')


#######################################################################################

def judul():
    print('Program Menghitung Volume dan Luas Permukaan Balok'.center(45))
    print('Bangun Ruang Balok'.center(45))
    print()

def inputan():
    p = float(input('Masukkan Panjang: '))
    l = float(input('Masukkan Lebar: '))
    t = float(input('Masukkan Tinggi: '))
    return p,l,t

def hitung(p,l,t):
    vol = p*l*t
    luas_surf = 2*(p*l + p*t + l*t)
    luas_non_tutup = luas_surf - p*l
    return vol,luas_surf,luas_non_tutup

def tampilan(pesan,nilai):
    print(f'Nilai {pesan} : {nilai}')

def pilihan():
    pilih = input('Apakah lanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Terima Kasih')
    return a

def main():
    print('Hallo')
    judul()                                      #judul
    p,l,t = inputan()                            #inputan
    vol,luas_surf,luas_non_tutup = hitung(p,l,t) #hitung
    #tampilan
    tampilan('Volume',vol)
    tampilan('Luas Permukaan',luas_surf)
    tampilan('Luas Permukaan tanpa Tutup',luas_non_tutup)
    a = pilihan()                                #pilihan
    return a
  
a = True
while a:
    a = main()
   
    

