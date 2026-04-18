import random
import string

# Taking user input
length = int(input("Enter the desired password length: "))

print("Choose password complexity:")
print("1. Only Letters")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Special Characters")

choice = input("Enter choice (1/2/3): ")

# Defining character sets
letters = string.ascii_letters
digits = string.digits
special = string.punctuation

# Selecting characters based on user choice
if choice == '1':
    characters = letters
elif choice == '2':
    characters = letters + digits
elif choice == '3':
    characters = letters + digits + special
else:
    print("Invalid choice!")
    exit()

# Generating password
password = ''.join(random.choice(characters) for _ in range(length))

# Displaying password
print("Generated Password:", password)