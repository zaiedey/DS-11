# Guess the number game
# create a random number between 1 and 100
# ask the user to guess the number
# if the guess is too high, tell the user
# if the guess is too low, tell the user
# if the guess is correct, tell the user and end the game
# keep track of the number of guesses
#what the dietrich.
import random
def guess_the_number():
    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    while guess != number:
        guess = int(input("Guess the number: "))
        attempts += 1
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print(f"Correct! The number was {number}")
            print(f"It took you {attempts} attempts")
