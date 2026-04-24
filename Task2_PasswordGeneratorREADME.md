## Password Generator (Python)

A simple command-line password generator built using Python. It allows users to create secure passwords based on selected complexity levels.

---

## Features

* User-defined password length
* Multiple complexity options
* Random password generation
* Supports letters, numbers, special characters
* Simple and interactive CLI

---

## Technologies Used

* Python 3
* Built-in `random` module
* Built-in `string` module

---

## How to Run

Clone the repository:

```id="p4k8zn"
git clone https://github.com/your-username/password-generator.git
```

Navigate to the project folder:

```id="v6t2qs"
cd password-generator
```

Run the Python file:

```id="k3mdx9"
python password.py
```

---

## How to Use

1. Enter the desired password length
2. Choose password complexity:

   * 1 → Only Letters
   * 2 → Letters + Numbers
   * 3 → Letters + Numbers + Special Characters
3. The program generates and displays a random password

---

## Game Logic

* Takes user input for length and complexity
* Selects character set based on choice
* Uses random selection to generate password
* Combines characters into a final string

---

## Sample Output

```id="d9q2xm"
Enter the desired password length: 8
Choose password complexity:
1. Only Letters
2. Letters + Numbers
3. Letters + Numbers + Special Characters
Enter choice (1/2/3): 2
Generated Password: aK9dP3xQ
```

---

## Source Code

```python id="m7s1hy"
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
```

---

## Future Improvements

* Add password strength indicator
* Save generated passwords to file
* GUI version using Tkinter
* Copy to clipboard feature

---

## License

This project is open-source.
