#!/usr/bin/env python3
l1 = [1, 2, 3, 4, 5]
l2 = [1, 3, 5, 7, 9]

common = []

print("Starting")
for x in l1:
    if x in l2:
        common.append(x)


print(f"list1: {l1}")
print (f"list2: {l2}")
print(f"Common elements are: {common}")
print("Ending")
