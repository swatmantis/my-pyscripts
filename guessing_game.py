#!/usr/bin/env python3
'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them 
whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

print ("****Let's play the Guessing Game****\nComputer will generate a random number between 1 and 9\nYou can take any number of attempts to guess the number\n")
rand_num = random.randint(1,9)

guess_count = 1
game_flag = "play"

while game_flag != "exit":
    usr_guess = int(input("Guess a number between 1 and 9: "))
    if usr_guess == rand_num:
        print ("\nYou have guessed the correct number {0} ! in {1} chances".format(rand_num,guess_count))
        break
    else:
        if usr_guess < rand_num:
            print ("Your guess is lower than the number")
        elif usr_guess > rand_num:
            print ("Your guess is higher than the number\n")
        guess_count += 1
        game_flag = input ("\nTry Again ?\nType 'yes' if you want to guess again. Type 'exit' if you want to quit: ")

        
    
