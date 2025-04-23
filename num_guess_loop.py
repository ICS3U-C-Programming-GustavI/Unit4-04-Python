#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 19, 2025
# This program executes a for loop for a number guessing game, which also uses break statements.

import random

# Generate a random number between 1 and 10
correct_number = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess the number (0 to 9): "))

        if guess == correct_number:
            print("You guessed it right!")
            break  # Exit the loop if correct
        else:
            print("Wrong guess, try again.")
    except ValueError:
        print("Invalid input! Please enter a whole number.")
