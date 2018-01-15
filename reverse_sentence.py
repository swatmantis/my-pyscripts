#!/usr/bin/env python3
"""
Created on Wed Jan 10 07:42:14 2018

@author: Swathi
"""
'''
Excercise: 15
--------------
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
'''

def reverse_Sentence(original_String):
    original_String = original_String.split(' ')
    new_String = []
    [new_String.append(word) for word in reversed(original_String)]
    return " ".join(new_String)
#    return new_String

str1 = input("Enter a sentence: ")
print ("Reversed string is: {}".format(reverse_Sentence(str1)))