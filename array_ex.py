#!/usr/bin/env python3
from array import array

numbers = array('i', [1, 2, 3])
numbers.insert(0, 4)
print(numbers)
