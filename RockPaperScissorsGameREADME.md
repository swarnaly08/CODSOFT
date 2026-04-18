## Rock Paper Scissors Game (Python)

A simple command-line Rock, Paper, Scissors game built using Python. The user plays against the computer, and scores are tracked across rounds.

---

## Features

* User vs Computer gameplay
* Random computer choice using Python's `random` module
* Score tracking system
* Input validation for user choices
* Option to play multiple rounds
* Final score display at the end

---

## Technologies Used

* Python 3
* Built-in `random` module

---

## How to Run

Clone the repository:

```
git clone https://github.com/your-username/rock-paper-scissors.git
```

Navigate to the project folder:

```
cd rock-paper-scissors
```

Run the Python file:

```
python game.py
```

---

## How to Play

Enter one of the following choices:

* rock
* paper
* scissors

### Rules:

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock

After each round:

* Score is updated
* You can choose to continue or exit

---

## Game Logic

* Computer randomly selects a choice
* Winner is determined based on standard rules:

  * Same choice → Tie
  * Winning combinations → User wins
  * Otherwise → Computer wins

---

## Sample Output

```
=== Rock, Paper, Scissors Game ===
Instructions: Type rock, paper, or scissors to play.

Enter your choice: rock
You chose: rock
Computer chose: scissors
You win this round!

Score -> You: 1 | Computer: 0
```

---

## Source Code

```python
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("=== Rock, Paper, Scissors Game ===")
    print("Instructions: Type rock, paper, or scissors to play.\n")

    while True:
        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please try again.\n")
            continue

        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!\n")
        elif result == "user":
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
        print()

# Run the game
play_game()
```

---

## Future Improvements

* Add GUI using Tkinter or PyQt
* Add difficulty levels (AI prediction)
* Multiplayer mode
* Sound effects

---

## License

This project is open-source.
