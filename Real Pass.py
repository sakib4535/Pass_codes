import string
import secrets

symbols = ['$', '@', '*', '^',')','#']
password = ""

for _ in range(10):
    password += secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
password += secrets.choice(symbols)
print(password)

