#!/usr/bin/env python3
l1 = [1, 2, 1, 3, 5, 4, 5, 7, 7, 7]

occurence = {}

print("Starting")
for num in l1:
    if num not in occurence:
        occurence[num] = l1.count(num)


print(f"list: {l1}")
print("Num  : Occurence ")

for k,v in occurence.items():
    print(f"{k} \t : \t\t{v}")
print("Ending")
