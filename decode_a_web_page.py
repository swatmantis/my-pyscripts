#!/usr/bin/env python3
"""
Created on Tue Jan 16 07:20:47 2018

@author: Swathi
"""
'''
Exercise 17 (and Solution)

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

'''

import re
import requests
from bs4 import BeautifulSoup

# some requests code here for getting r_html 
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html,"lxml")
headings = soup.find_all(class_="story-heading")
#print (heading)

# Extracting the link using Beautiful Soup
i = 1
print ("********** Using Beautiful Soup**********\n\n\n")
for heading in headings:
    if heading.a:
        print ("BSTitle #{0} : {1}".format(i,heading.a.text.replace("\n", " ").strip()))
#        print (heading.a.text.replace("\n", " ").strip())
    else:
        print ("Title #{0} : {1}".format(i,heading.contents[0].strip()))
#        print(heading.contents[0].strip())
    i += 1

# Extracting the link using Regex
i = 1
print ("\n\n\n********** Using Regex **********\n\n\n")
for heading in headings:
    regex = r"<a.*>(\s*.*)<\/a"
    match = re.search(regex,str(heading))    
    if match: 
        print ("RegTitle #{0} : {1}".format(i,match.group(1).strip()))
        i += 1