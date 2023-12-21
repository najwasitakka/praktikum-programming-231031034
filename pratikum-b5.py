nim = [2,3,1,0,3,1,0,3,4]
print(nim)

# akses item
print('item indeks 0:', nim[0])
print('item indeks 3:', nim[3])
print('item indeks terakhir:', nim[len(nim)-1])

# akses indeks negatif
print('item indeks terakhir:', nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6]', nim[-6])
print('item indeks 5: [-4]', nim[-4])
print('item indeks -7: [2]', nim[2])
print('item indeks 3: [-7]', nim[-7])

# akses indeks batas
print(f'item indeks 1,2,.....: {nim[1:]}')
print(f'item indeks 3,4,.....: {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[-1]}')
print(f'item indeks [:4]: {nim[-5]}')

# pengirisan
print(f'item indeks 1,2:{nim[1:3]}')
print(f'item indeks []:{nim[3:3]}')
print(f'item indeks 2,3,4:{nim[2:5]}')
print(f'item indeks [1:8]:{nim[1:-1]}')
print(f'item indeks [2:7]:{nim[2:-2]}')

# Nested List
kelas = [('Matkul1',2),
         ('Matkul2',3)]
print(kelas)
kelas.append(('Matkul3',2))
print(kelas)

# tambahkan matkul 4 dan 5 dan sksnya

# Mata kuliah 1: Matkul1 dengan 2 sks
# Mata kuliah 2: Matkul1 dengan 3 sks
# Mata kuliah 3: Matkul1 dengan 2 sks
# Mata kuliah 4: Matkul1 dengan .. sks
# Mata kuliah 5: Matkul1 dengan .. sks


