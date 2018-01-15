#!/usr/bin/env python3
"""
Created on Mon Jan 15 07:26:16 2018

@author: Swathi
"""
'''
Write a function called drawSquare that is responsible for having some turtle draw a square of some size. 
The actual turtle and the actual size of the square were defined to be provided as parameters.
'''

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():                      # Define the main function
    wn = turtle.Screen()         # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()       # create alex
    drawSquare(alex, 50)         # Call the function to draw the square

    wn.exitonclick()

if __name__ == "__main__":
    main()                           # Invoke the main function