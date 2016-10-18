# -*- coding: utf-8 -*-
"""
Created on Fri May 06 14:10:12 2016

@author: MaGesh
"""

def DataScience(listOfStrings):
    returnStr=""
    for word in listOfStrings:
        word+="DataScience"
        returnStr+=word+"\n"
    return returnStr

x=["Magesh","Prabhu"]
print DataScience(x)