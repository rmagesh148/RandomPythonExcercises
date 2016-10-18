# -*- coding: utf-8 -*-
"""
Created on Sat May 07 11:25:27 2016

@author: MaGesh
"""


def is_palindrome(string):
    string.split()
    listOfWords=map((lambda x: x.lower()),string)
    return reduce((lambda x,y:x+y),listOfWords)==reduce((lambda x,y:y+x),listOfWords)


string="test string"
if is_palindrome(string):
    print "Yes"
else:
    print "No"

