#!/usr/bin/env python3
"""Find Greatest Common Factor"""
import random

def generate_random_numbers(start, stop, count):
    random_numbers = []
    for number in range(1, count + 1):
        # start = 2
        # stop = 1000
        random_numbers.append(random.randint(start, stop))
    return random_numbers

def calculate_factors(number):
    factors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            quotient = int(number / divisor)
            factors.append(divisor)
    factors.sort()
    return factors

def calculate_GCF(first, second):
    #Finding the factors of a the given numbers
    first_factors = set(calculate_factors(first))
    second_factors = set(calculate_factors(second))

    print(f"Factors of {first}: {first_factors}")
    print(f"Factors of {second}: {second_factors}")

    gcf = max(first_factors & second_factors)
    return gcf

def main():
    #Generating two random numbers
    # first, second = 10, 20
    first, second = generate_random_numbers(2, 50, 2)

    #Find and print Greatest Common Factor
    gcf = calculate_GCF(first, second)
    print(f"Greatest Common Factor of {first} and {second} is: {gcf}")

if __name__ == '__main__':
    main()
