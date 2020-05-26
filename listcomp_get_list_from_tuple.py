#!/usr/bin/env python3
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 15)
]
# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(f"Prices: {prices}")

# filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]

print(f"Items with price >= 10: {filtered}")
