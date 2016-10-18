# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 15:19:14 2016

@author: MaGesh
"""
def convertPolynomial(listValue,other):
        degreeOfSelf = len(listValue)
        degreeOfOther = len(other)
        if degreeOfSelf == degreeOfOther:
            return listValue,other
        else:
            difference = abs(degreeOfSelf-degreeOfOther)
            if degreeOfSelf > degreeOfOther:
                for i in range(0,difference):
                    other.insert(i,0)
                return listValue,other
            else:
                for i in range(0,difference):
                    listValue.insert(i,0)
                return listValue,other
                
class Polynomial:
    coeffs = []
    def __init__(self,coefficients):
        self.coeffs = coefficients
    def coeff(self,i):
        maxCoeff = len(self.coeffs)
        coeffToBeCalled = maxCoeff - 1
        return self.coeffs[coeffToBeCalled - i]                
    def add(self,other):
        newPoly=[]
        newPolynomial = self.coeffs        
        other=other.coeffs
        newPolynomial,otherPolynomial = convertPolynomial(newPolynomial,other)
        for i in range(0,len(newPolynomial)):
            print i
            newPoly.append(newPolynomial[i] + otherPolynomial[i])
        return newPoly
    def __add__(self,v):
        return self.add(v)
                
    def mul(self,other):
        final_coeff= [0]*(len(self.coeffs) + len(self.coeffs) - 1)
        for ind1, coeffs1 in enumerate(self.coeffs):
            for ind2, coeffs2 in enumerate(other.coeffs):
                final_coeff[ind1+ind2]+=coeffs1*coeffs2
        return final_coeff
    def __mul__(self,v):
        return self.mul(v)
    def val(self,value):
        maxLength=len(self.coeffs) -1
        sumValue=0
        for i in range(0,len(self.coeffs)):
            sumValue+=self.coeffs[i]*(value**maxLength)
            maxLength=maxLength-1
        return sumValue


        
        
        
        
        