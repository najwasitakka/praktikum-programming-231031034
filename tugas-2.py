J = True
H = False

print()
hasil = J & J
print(J,"and",J,"adalah =",hasil)
hasil = J & H
print(J,"and",H,"adalah =",hasil)
hasil = H & J
print(H,"and",J,"adalah =",hasil)
hasil = H & H
print(H,"and",H,"adalah =",hasil)

print()
hasil = J | J
print(J,"or",J,"adalah =",hasil)
hasil = J | H
print(J,"or",H,"adalah =",hasil)
hasil = H | J
print(H,"or",J,"adalah =",hasil)
hasil = H | H
print(H,"or",H,"adalah =",hasil)

print()
hasil = J ^ J
print(J,"xor",J,"adalah =",hasil)
hasil = J ^ H
print(J,"xor",H,"adalah =",hasil)
hasil = H ^ J
print(H,"xor",J,"adalah =",hasil)
hasil = H ^ H
print(H,"xor",H,"adalah =",hasil)

print()
hasil = not J
print("not",J,"adalah =",hasil)
hasil = not H
print("not",H,"adalah =",hasil)
