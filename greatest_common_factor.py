#!/usr/bin/env python3
"""Find Greatest Common Factor"""
import random

def get_random_num():
    start = 2
    stop = 50
    return random.randint(start, stop)

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def main():
    #Generating two random numbers
    m = get_random_num()
    n = get_random_num()

    #Find and print Greatest Common Factor
    print (f"gcd of {m} and {n} is {gcd(m, n)}")

if __name__ == '__main__':
    main()
