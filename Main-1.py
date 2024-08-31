import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Introduce la longitud de la contraseña: "))

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Tu contraseña generada es:", password)
