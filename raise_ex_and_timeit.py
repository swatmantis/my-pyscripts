#!/usr/bin/env python3
#Timeit is the module that'll caclulate time to execution
from timeit import timeit

code1 = """
def xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    xfactor = 10 / age
    print(xfactor)

try:
    xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = xfactor(-1)
if xfactor == None:
  pass
"""

print("code1 =", timeit(code1, number = 10000))
print("code1 =", timeit(code2, number = 10000))
