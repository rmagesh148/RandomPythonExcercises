# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:47:47 2016

@author: MaGesh
"""
"""class Word(object):
    def __init__(self,string,i):
        self.string = string
        self.index = i"""

def createDupArray(words,size):
    dupArray=[]
    for i in xrange(size):
        dupArray.append(words[i])
    return dupArray

def printAnagrams(word,size):
    
    dupArray=createDupArray(word,size)
    print word
    
    for i in xrange(size):
        dupArray[i] = ''.join(sorted(dupArray[i]))
    
    for i in range(0,len(dupArray)):
        print dupArray[i]
        
    print("############################")
  
    dupArrayN = sorted(range(len(dupArray)),key = lambda k:dupArray[k])
    print dupArrayN    
    return dupArrayN
    
   
    
        



words=["cat","dog","cta","god","act"]
size=len(words)
for i in xrange(size):
    print i
    print words[i]
ind=printAnagrams(words,size)
for i in ind:
    print words[i]

    
    