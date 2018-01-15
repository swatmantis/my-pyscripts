#!/usr/bin/env python3
filename = input ("Enter a filename (with extension): ")
#ext=filename.split(".")
#print ("Filename extension is: " + ext[-1])
print ("Filename extension is: " + filename.split(".")[-1])
