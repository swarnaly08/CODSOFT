## Calculator (Python)

A basic command-line calculator built using Python. It performs arithmetic operations based on user input.

---

## Features

* Supports basic arithmetic operations
* User-friendly command-line interface
* Handles invalid inputs
* Prevents division by zero errors
* Quick and simple calculations

---

## Technologies Used

* Python 3

---

## How to Run

Clone the repository:

```id="b7k2fd"
git clone https://github.com/your-username/simple-calculator.git
```

Navigate to the project folder:

```id="x4mzq1"
cd simple-calculator
```

Run the Python file:

```id="p9r6tn"
python calculator.py
```

---

## How to Use

1. Enter the first number
2. Enter the second number
3. Choose an operation:

   * 1 → Addition (+)
   * 2 → Subtraction (-)
   * 3 → Multiplication (*)
   * 4 → Division (/)
4. The result will be displayed

---

## Game Logic

* Takes two numerical inputs from the user
* Displays operation choices
* Performs calculation based on selected option
* Handles division by zero separately
* Displays the final result

---

## Sample Output

```id="z8q1ls"
Enter first number: 10
Enter second number: 5
Choose operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
Enter choice (1/2/3/4): 1
Result: 15
```

---

## Source Code

```python id="n2d8xp"
# Simple Calculator in Python

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Performing calculation
if choice == '1':
    result = num1 + num2
    print("Result:", result)

elif choice == '2':
    result = num1 - num2
    print("Result:", result)

elif choice == '3':
    result = num1 * num2
    print("Result:", result)

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid choice. Please select a valid operation.")
```

---

## Future Improvements

* Add more operations (modulus, power)
* GUI version using Tkinter
* Continuous calculation mode
* Input validation improvements

---

## License

This project is open-source.
