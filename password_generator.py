# Import the random module
import random

# Define the possible characters for the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

# Ask the user for the desired password length
length = int(input("Entrez la longueur souhaitée du mot de passe: "))

# Generate password
password = ''
for i in range(length):
    password += random.choice(characters)

# Show password to user
print("Le mot de passe généré est:", password)
