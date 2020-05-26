#!/usr/bin/env python3
#Python program to write into and read from a csv file

import csv

with open("data.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "gender"])
    writer.writerow(["Swathi", 15, "F"])
    writer.writerow(["Santosh", 25, "M"])

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
