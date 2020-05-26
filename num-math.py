# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:01:50 2017

@author: Swathi
"""
#Math of numbers
#Script to input two numbers and add, subtract, multiply, divide (quotient/remainder) them as a float

x = float(input ("Enter the value of x: "))
y = float(input ("Enter the value of y: "))

print ("\nSum of x and y: ", x+y)
print ("Difference of x and y: ", x-y)
print ("Product of x and y: ", x*y)
print ("Quotient/Remainder of x and y: ", x/y)


print ("\n\nSum: {}".format(x + y))
print ("Difference: {}".format(x - y))
print ("Product: {}".format(x * y))
print ("Division: {:.2f}".format(x/float(y)))
