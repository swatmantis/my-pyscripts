#!/usr/bin/env python3

#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

#input comma separated numbers
#num = input ("Enter comma separated numbers: ")
list1 = input ("Enter comma separated numbers: ").split(",")
#list1 = num.split(",")
print ("Numbered list: ",list1)

#append to a list
list1.append(23)
print ("\n After appending 23 to list: ",list1)


#Tuple Calculations#
tup = tuple(list1)
print ("\nTuple: ",tup)
print ("\nFirst tuple element: {0} \n Last tuple element: {1}".format(tup[0],tup[-1]))
#print first and last elements of the tuple

#append to a tuple - shouldn't work
#print ("\n Trying to append:",tup.append[45])
