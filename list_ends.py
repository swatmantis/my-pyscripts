#!/usr/bin/env python3
"""
Created on Tue Jan  9 07:03:31 2018

@author: Swathi
"""
'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.'''

import random

def list_ends(rlist):
    if len(rlist) > 1:
        return [rlist[0], rlist[-1]]
    else:
        return rlist
    
l1 = random.sample(range(100),random.randint(1,20))
print ("List of length {0} is: {1}\n".format(len(l1),l1))

l2 = list_ends(l1)
print ("List ends are: {}\n".format(l2))