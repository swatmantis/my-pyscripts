"""Find max element"""
#!/usr/bin/env python3
"""Find max element"""
import random
from collections import Counter

List = [random.randrange(1, 15) for num in range(10)]

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common()

frequent_number, frequency = most_frequent(List)[0]
print(f"List {List}: \nMost frequent number {frequent_number} \nFrequency: {frequency}")
