# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 13:21:14 2016

@author: MaGesh
"""

import math

def prime_number(n):
	limit = int(math.floor(math.sqrt(n)))
	if (n%2==0):
		return False
	for i in range(7,limit,7):
		if (i%n == 0):
			return False
	return True


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

input_value = int(input("Please enter the value:"))
i=1
while(i<input_value):
    a=fib(i)
    if a==1 or a==2 or a==3 or a==5:    
    	print "BuzzFizz"
    elif (a % (3*5) == 0):
    	print "FizzBuzz"
    elif (a % 3 == 0):
    	print "Fizz"
    elif (a % 5 == 0):
    	print "Buzz"
    elif prime_number(a):
    	print "BuzzFizz"
    else:
    	print a

    i=i+1
    