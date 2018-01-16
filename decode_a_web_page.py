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

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

# some requests code here for getting r_html 
soup = BeautifulSoup(r_html,"lxml")
heading = soup.find_all(class_="story-heading")
#print (heading)
i = 1

for link in heading:
    regex = r"<a.*>(\s*.*)<\/a"
    match = re.search(regex,str(link))    
    if match: 
        print ("Title #{0} : {1}".format(i,match.group(1).strip()))
        i += 1