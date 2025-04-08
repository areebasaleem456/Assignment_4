import random

def guess_the_num():
    comp_guess = random.randint(1, 20)
    attempts = 7

    print("I am thinking of a number between 1 and 20.")

    while attempts > 0:
        print(f"You have {attempts} tries.")
        try:
            user_guess = int(input("Try any number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_guess > comp_guess:
            print("Try a lower number...")
        elif user_guess < comp_guess:
            print("Try a higher number...")
        else:
            print(f"Congrats! You guessed it right in {7 - attempts + 1} tries.")
            return

        attempts -= 1  # Decrease the number of attempts

    # When attempts are finished
    print(f"No more chances left. The number was {comp_guess}.")

# Run the game
guess_the_num()
    