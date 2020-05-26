#!/usr/bin/env python3
def xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    xfactor = 10 / age
    print(xfactor)

try:
    xfactor(-1)
except ValueError as error:
    print(error)
