#!/usr/bin/env python3
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num  = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))
if (num % 2 == 0):
	if (num % 4 == 0):
		print ("Your number is a multiple of 4\n")
	else:
		print ("It is an even number but not a multiple of 4\n")
else:
	print ("It is an odd number\n")

if (num % check == 0):
	print ("Your number {0} is divisible by {1}\n".format(num, check))
else:
	print ("Your number {0} is not divisible by {1}\n".format(num, check))
	
