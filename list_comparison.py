#!/usr/bin/env python3
#Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(30), 7)
b = random.sample(range (30), 12)
c = []
#for key in a:
#	if key in b and key not in c:
#		c.append(key)
#one liner
[c.append(key) for key in a if key in b and key not in c]
print ("a={0}\nb={1}\nCommon elements are: {2}\n".format(a,b,c))
