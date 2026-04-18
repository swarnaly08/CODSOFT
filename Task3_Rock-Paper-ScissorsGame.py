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
