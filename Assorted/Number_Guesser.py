# Guess a number that is randomly generated

import random

top_of_range = input("type a number greater than zero: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("please put in a number greater than zero next time.")
    quit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please put in a number greater than zero next time.")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("You were below the number!")

print("You got in", guesses, "guesses!")