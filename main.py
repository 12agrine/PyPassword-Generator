import random
from characters import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Simple Version
password = ""

for char in range(1, num_letters + 1):
    password += random.choice(letters)
for char in range(1, num_symbols + 1):
    password += random.choice(symbols)
for char in range(1, num_numbers + 1):
    password += random.choice(numbers)

print(f"Here is your password: {password}")

# Complex Version
password_list = []

for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password}")
