"""
Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""
import random
def guess_the_number():
    print("Hello! Whst is your name?")
    name = input()

    print("Well, ",name," I am thinking of a number between 1 and 20")
    secret_number = random.randint(1, 20)

    guesses_taken = 0

    while True:
        print()
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Good job", name, "! You guessed my number in ", guesses_taken, "guesses!")
            break

guess_the_number()