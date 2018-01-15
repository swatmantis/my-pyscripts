#!/usr/bin/env python3
"""
Created on Sun Oct  8 22:01:50 2017

@author: Swathi
"""
'''Question: Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''

l1 = input("Enter few numbers separated by comma: ").split(",")
#l1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = []
[even_list.append(num) for num in l1 if int(num) % 2 == 0]
print ("Even elements in the list are {0}".format(even_list))

