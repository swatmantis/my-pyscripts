#!/usr/bin/env python3

#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

str = input ("Enter a string for a palindrome test: ")
if len(str)%2 == 0:
	first = str[0:int(len(str)/2)].lower()
else:
	first = str[0:int(len(str)/2+1)].lower()
second = str[int(len(str)/2):].lower()
# reversing a string
rsecond = second[::-1]

if first == rsecond:
	print ("{0} is a palindrome".format(str))
else:
	print ("{0} is not a palindrome".format(str))
