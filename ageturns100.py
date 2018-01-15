#!/usr/bin/env python3
import datetime
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells#them the year that they will turn 100 years old.
#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name, age, num = input("Enter your name,age and a random number (Format:<Name> <Age> <Number>): ").split()
age = int(age)
num = int(num)

years_to_100 = 100 - age
now = datetime.datetime.now()
curr_year = now.year
year_of_100 = curr_year + years_to_100
str = "Hello {0} ! Congratulations, you are {1} years away from hitting a century! You will turn 100 in the year \"{2}\"\n".format(name,years_to_100,year_of_100)
print (str*num)

