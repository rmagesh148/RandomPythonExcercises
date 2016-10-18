# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 12:19:37 2016

@author: MaGesh
"""
import re
def shortestPrefix(nums,limit):
    addArrayPrefixes=[]
    for numbers in nums:
        length=len(numbers)
        i=0
        while(i<=length):
            addArrayPrefixes.append(numbers[0:i])
            i=i+1
    removeDuplicatesArray=[]
    removeDuplicatesArray=[x for x in addArrayPrefixes if addArrayPrefixes.count(x) ==1 ]
    print removeDuplicatesArray
    for words in nums:
        for w in removeDuplicatesArray:
            len(re.findall(w,words))
                        
                
def main():
    nums=['1234','1256','463']
    limit=10
    listOfValues = shortestPrefix(nums,limit)

if __name__ == "__main__":
    main()
        
