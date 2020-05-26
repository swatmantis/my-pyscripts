#!/usr/bin/env python3
#Program to find the characters that repeats the most
""" Max element of a given list"""
import random

start = 1
stop = 6
limit = 10

#Generating a list of random elements with duplicates
elements = [random.randrange(start, stop) for num in range(limit)]
print("list is: ", elements)

#Creating a list of tuples of (number, occurence)
count = [(num, elements.count(num)) for num in set(elements)]
sorted_count = sorted(count, key=lambda kv: kv[1], reverse=True)
print(f"sorted count matrix: {sorted_count}\n")

#Printing the highest occurence number
#If there is only one number with highest occurence
if sorted_count[0][0] > sorted_count[1][0]:
    print(f"\nNumber {sorted_count[0][0]} repeated the most of {sorted_count[0][1]} times")
#If there are multiple numbers with the same highest occurence
else:
    for count in sorted_count:
        if count[1] == sorted_count[0][1]:
            print(f"\nNumber {count[0]} repeated the most of {count[1]} times")
