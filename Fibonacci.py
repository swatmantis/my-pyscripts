#!/usr/bin/env python3
"""
Created on Tue Jan  9 07:29:33 2018

@author: Swathi
"""
'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
'''
fib = []
def get_fiblength():
    return int(input("How many Fibonacci numbers would you like to generate ? "))
    
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

length = get_fiblength()
fibseries = []
i = 0
while i <= length:
    print ("Iteration #{}".format(i))    
    fibseries.append(fib(i))
    print ("Current Fibseries = {}".format(fibseries))
    i += 1

print ("\nFinal Fibonacci Series of length {0}: {1}".format(length,fibseries))
#print ("Fib({0}) = {1}".format(length,fib(length)))