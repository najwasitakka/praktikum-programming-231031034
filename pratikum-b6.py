a = True
i = 0
limit = 3

while a:
    i += 1      # i = 1
    if i <= limit:
        print('Selamat Bergabung')
    else:
        a = False


###################################################
print()
a = True
i = 0
limit = 3

while a:
    i += 1      # i = 1
    if i <= limit:
        print('Selamat Bergabung',i)
    else:
        a = False


##################################################
print()
a = True
i = 0
limit = 3

while a:
    i += 1      # i = 1
    if i <= limit:
        print('Selamat Bergabung',limit-i+1)
    else:
        a = False
