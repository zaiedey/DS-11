import random

number = random.randint(1, 100)
guess = None
previous_guess = None
guesses = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))

    if previous_guess is not None:
        if abs(guess - number) < abs(previous_guess - number):
            print("You're getting closer!")
        elif abs(guess - number) > abs(previous_guess - number):
            print("You're getting farther!")

    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")

    guesses += 1
    previous_guess = guess

print("Correct! You took", guesses, "guesses.")
