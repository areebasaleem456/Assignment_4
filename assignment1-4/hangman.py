# Hangman Game in Python
import random

words = ["variable", "function", "list", "tuple", "dictionary", "set", "string", "integer", "float", "boolean", "class", "object", "method", "module", "import", "lambda", "exception", "try", "except", "if", "else", "elif", "for", "while", "break", "continue", "return", "def"]

word = random.choice(words)
guess_letters = []
attempts = 8

# Hangman visuals for each wrong guess
hangman_pics = [
    '''
     ------
     |    |
          |
          |
          |
          |
          |
    ''', 
    '''
     ------
     |    |
     O    |
          |
          |
          |
          |
    ''', 
    '''
     ------
     |    |
     O    |
     |    |
          |
          |
          |
    ''', 
    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
          |
    ''', 
    '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
          |
    ''', 
    '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
          |
    ''', 
    '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
          |
    '''
]

print("Welcome to Hangman Game..")
print("A simple console-based Hangman game where the player guesses letters to form a word")

print("_" * len(word))

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guess_letters:
        print("You already guessed that letter.")
        continue

    guess_letters.append(guess)

    if guess in word:
        print("Good job!")
    else:
        attempts -= 1
        print("Wrong guess!")
    
    current_word = "".join([letter if letter in guess_letters else "_" for letter in word])
    print(current_word)

    # Display the hangman based on wrong attempts, preventing out-of-range error
    print(hangman_pics[min(len(hangman_pics) - 1, 8 - attempts)])

    if "_" not in current_word:
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("Sorry, you're out of attempts. The word was:", word)
