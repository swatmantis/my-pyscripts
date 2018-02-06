#!/usr/bin/env python3
"""
Created on Mon Feb  5 08:04:43 2018

@author: Swathi
"""
'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
 and another number. The function decides whether or not the given number is inside the list and returns (then prints) 
 an appropriate boolean.

Extras:

    Use binary search.
'''

def find_By_BinarySearch(num,search_List):
    'Searching num in search_List using Binary Search algorithm'
    foundNum = "False"

    mid = int(len(search_List)/2)
    
    'Starting the search'
    while len(search_List) >= 1:
#        print ("search_List = {}".format(search_List))
#        print ("mid = {}".format(mid))
#        print ("search_List[mid] = {}".format(search_List[mid]))
        if int(search_List[mid]) == num:
#            print("mid = num")
            foundNum = "True"
            return foundNum
        
        elif int(search_List[mid]) < num:
#            print("mid < num")
            search_List = search_List[mid+1:]
            return find_By_BinarySearch(num,search_List)
        
        elif int(search_List[mid]) > num:
#            print("mid > num")
            search_List = search_List[:mid]
            return find_By_BinarySearch(num,search_List)


if __name__=="__main__":
    oList = input("Enter an array of numbers (comma separated): ").split(',')
    'Converting oList into an Ordered List'
    oList.sort() 
    'Input a search number'
    num = int(input("Enter a number to search: "))
    
    if find_By_BinarySearch(num,oList):
        print ("\nNumber {} is in the list {}\n".format(num,oList)) 
    else:
        print ("\nNumber {} is NOT in the list {}\n".format(num,oList))