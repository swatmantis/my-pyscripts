#!/usr/bin/env python3
#Program to find the characters that repeats the most
from pprint import pprint
sentence = "This is a common inteview question"

occurence = {}

for char in sentence:
    if char not in occurence:
        occurence[char] = sentence.count(char)

# pprint(occurence, width=1)

occurence_sorted = sorted(occurence.items(), key=lambda kv: kv[1], reverse=True)

pprint(occurence_sorted)
print("max_frequency_char =", occurence_sorted[0])
