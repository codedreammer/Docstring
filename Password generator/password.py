import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
while True:
    try:
        length = int(input("Enter length: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
password = ""

for _ in range(length):
    password += random.choice(chars)

print(password)