#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = int(input("How many letters do you want ? :"))
n_numbers = int(input("How many numbers do you want ? :"))
n_symbols = int(input("How many symbols do you want ? :"))

password = []
for _ in range(n_letters):
    password.append(letters[random.randint(0, len(letters) -1)])
for _ in range(n_numbers):
    password.append(numbers[random.randint(0, len(numbers) -1)])
for _ in range(n_symbols):
    password.append(symbols[random.randint(0, len(symbols) -1)])

random.shuffle(password)
password_generated = ""
for content in password:
    password_generated += content
print(f"Your password : {password_generated}")