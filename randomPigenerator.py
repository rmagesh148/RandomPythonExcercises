# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:13:06 2016

@author: MaGesh
"""

import random
def randomGenerator(aLargeNumber):
    nSuccess = 0;
    nThrows=0;
    x = 0;
    y = 0;
    for i in range(0,aLargeNumber):
        x=random.random()
        y=random.random()
        nThrows = nThrows + 1
        if (x**2 + y**2 <= 1):
            nSuccess = nSuccess +1
    print(nSuccess)
    print(nThrows)
    print(4*(float(nSuccess)/float(nThrows)))
    
randomGenerator(1000000)