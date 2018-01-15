#!/usr/bin/env python3
'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

playagain_flag = "yes"
print ("Alright. Let's play Rock-Paper-Scissors game.\n")
while playagain_flag == "yes":  
    p1_lower = input("Player 1 input (Rock/Paper/Scissors): ").lower()
    p2_lower = input("\nPlayer 2 input (Rock/Paper/Scissors): ").lower()
#    p1_lower = p1_lower.lower()
#    p2_lower = p2_lower.lower()
    if p1_lower == "rock":
        if p2_lower == "scissors":
            print ("Player 1 wins !\n")
        elif p2_lower == "paper":
            print ("Player 2 wins !")
        elif p2_lower == "rock":
            print ("It's a draw !")
        else:
            print ("Typo encountered. Let's restart the game.")
            continue
            
    if p1_lower == "paper":
        if p2_lower == "scissors":
            print ("Player 2 wins !\n")
        elif p2_lower == "paper":
            print ("It's a draw !")
        elif p2_lower == "rock":
            print ("Player 1 wins !")
        else:
            print ("Typo encountered. Let's restart the game.")
            continue
            
    if p1_lower == "scissors":
        if p2_lower == "scissors":
            print ("It's a draw!\n")
        elif p2_lower == "paper":
            print ("Player 1 wins !")
        elif p2_lower == "rock":
            print ("Player 2 wins !")
        else:
            print ("Typo encountered. Let's restart the game.")
            continue

    playagain_flag = input("Would you like to play another round (yes/no) ? ")
    if playagain_flag == "no":
        print("Ok, quitting the game. Bye !\n")