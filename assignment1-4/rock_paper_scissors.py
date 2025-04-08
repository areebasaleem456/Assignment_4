import random

def rock_paper_scissors():
    # Get the computer's choice
    computer_choice = random.choice(['r', 'p', 's'])
    
    # Get the user's choice
    user_choice = input("Select R for Rock, P for Paper, S for Scissors: ").lower()

    # Validate user input
    if user_choice not in ['r', 'p', 's']:
        print("Invalid choice. Please select 'r', 'p', or 's'.")
        return

    # Display choices
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f"You chose {choices[user_choice]}, Computer chose {choices[computer_choice]}.")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You won!")
    else:
        print("You lost!")

# Run the game
rock_paper_scissors()