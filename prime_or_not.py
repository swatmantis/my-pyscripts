#!/usr/bin/env python3
"""
Created on Tue Jan  9 06:37:33 2018

@author: Swathi
"""
'''Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.).'''

def get_number(text="Type a number for prime check: "):
    return (int(input(text)))

def is_prime(num):
    divisors = [key for key in range(1,num+1) if num%key == 0]
    if len(divisors) > 2:
        print ("{} is not a prime number\n".format(num))
    else:
        print ("{} is a prime number\n".format(num))
    return divisors
    
num = get_number()
divisors = is_prime(num)
print ("Divisors are: {}".format(divisors))

