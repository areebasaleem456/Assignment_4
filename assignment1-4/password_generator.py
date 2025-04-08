import random 
import string

def password_generate(length =12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(character) for _ in range(length))
    return password

#user input
length = int(input("Enter the length of your desired password:"))

password = password_generate(length)
print("Your Desired Generated Password:", password)