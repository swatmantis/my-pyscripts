#!/usr/bin/env python3
# Program to find the Median of a given list
""" Median of a list"""
import random

start = 1
stop = 15
limit = random.randint(3, 10)

#Generating a list of random elements with duplicates
elements = random.sample(range(start, stop), limit)
print("list is: ", elements)

#Sorting the list
elements.sort()
# print("\nSorted list is:", elements)

#Find median
#If length of the list is odd, median is the middle element
length = len(elements)
if length % 2 == 1:
    median = elements[int((length - 1)/2)]
#If length of the list is even
else:
    median = (elements[int(length/2) - 1] + elements[int(length/2)])/2

print (f"median = {median}")
