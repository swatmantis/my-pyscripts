#!/usr/bin/env python3
"""
Created on Tue Jan  9 06:14:06 2018

@author: Swathi
"""
'''
Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.


'''

import random
#list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
final = []

list1 = random.sample(range(30),7)
list2 = random.sample(range(30),10)
print ("list1: {0}".format(list1))
print ("list2: {0}".format(list2))

[final.append(key) for key in list1 if key in list2 and key not in final]
print ("Common elements: {0}".format(final))