import random

print("I am thinking a number between 1 till 20")
#generate radom number
def num_guess_game():
    number= random.randint(1, 20)
    attempt=0
    max_tries = 7


    while attempt < max_tries :
        guess= int(input("Enter your guess number:"))
        attempt +=1
        if guess >number :
            print("Hint: Try lower number..")
        elif number >guess :
            print("Hint: Try higher number..")
        else:
            print(f"Congratulations! You guess right in {attempt} tries")
            return
        print(f"You have {max_tries - attempt} tries left.")

    print(f"No more chance. Generated number was {number}")
        
num_guess_game()