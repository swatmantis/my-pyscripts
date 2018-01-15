#!/usr/bin/env python3
"""
Created on Wed Jan 10 07:02:55 2018

@author: Swathi
"""
'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
import random
import numpy as np

def generate_dup_list(rng,length):
#    return random.sample(range(rng),length)
    return np.random.choice(rng, length, replace=True)

def remove_Duplicate(sample_list):
    #Removing Duplicates using sets
    unique_list = set(sample_list)
    
    #Remvoing Duplicates using list
#    unique_list = []
#    [unique_list.append(key) for key in sample_list if key not in unique_list]
    
    return unique_list

list1 = generate_dup_list(5,6)
#list1 = [2, 3, 6, 10, 56, 3, 35, 50, 10]
print ("Sample list: {}".format(list1))
print ("\n Unique list: {}".format(remove_Duplicate(list1)))

