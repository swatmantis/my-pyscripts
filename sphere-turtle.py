#!/usr/bin/env python3
import turtle

toy = turtle.Pen()
for i in range(1, 40):
    if i % 3 == 0:
        toy.color("black", "red")
        toy.hideturtle()
        toy.begin_fill()
        toy.circle(100)
        toy.end_fill()
    elif i % 3 == 1:
        toy.color("black", "orange")
        toy.hideturtle()
        toy.begin_fill()
        toy.circle(100)
        toy.end_fill()
    else:
        toy.color("black", "green")
        toy.hideturtle()
        toy.begin_fill()
        toy.circle(100)
        toy.end_fill()

    toy.right(10)
    toy.forward(5)
