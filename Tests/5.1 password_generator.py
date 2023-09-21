import random
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbol would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

lettersa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbersa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolsa = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

for _ in range(1, letters + 1):
    password += random.choice(lettersa)
for _ in range(1, symbols + 1):
    password += random.choice(symbolsa)
for _ in range(1, numbers + 1):
    password += random.choice(numbersa)

print(password)