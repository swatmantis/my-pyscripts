#!/usr/bin/env python3
"""
Created on Sun Jan 14 14:54:16 2018

@author: Swathi
"""
'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of 
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password 
every time the user asks for a new password. Include your run-time code in a main method.

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
import random
import string

def generate_strong_password(length): 
    splchars = '@&$!#'
    char = string.ascii_letters + string.digits + splchars
    pwd = random.sample(char, length)
    
    #Checking to confirm if the generated password has at least one digt and one special character
    if any(char.isdigit() for char in pwd) == False or any(char in splchars for char in pwd) == False:
        return generate_strong_password(length)
    else:
        return "".join(pwd)

    
def generate_weak_password():
    pwds = ['Itis1Apple', 'Password123', 'Ch@ngeme']
    return random.choice(pwds)

def main():
    while (True):
        usr_choice = input("Type 1 for strong password\n2 for a weak password\nq to Quit: \n")
        if usr_choice == '1':
            length = int(input("Enter the length of your password: "))
            print ("Password is: {}".format(generate_strong_password(length)))
        elif usr_choice == '2':
            print ("Password is: {}".format(generate_weak_password()))
        elif usr_choice == 'q':
            print ("Quitting. Bye !\n")        
            break
        else:
            print ("Incorrect input. Try again.")
    
if __name__ == '__main__':
    main()

                    
                    