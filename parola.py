import random
karakterler = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
sifre_uzunlugu = int(input('Şifre Uzunluğu:'))
sifre =8
''
for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print(sifre)