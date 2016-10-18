# -*- coding: utf-8 -*-
"""
Created on Fri May 06 14:06:42 2016

@author: MaGesh
"""

import numpy as np

def ols(X,y):
    n=X.shape[1]
    lambdaValue=0.5
    regMatrix=np.identity(n)
    regMatrix[0,0]=0
    XTX = X.T.dot(X) + lambdaValue * regMatrix
    invXtX = np.linalg.inv(XTX)
    XtX_xT = invXtX.dot(X.T)
    theta = XtX_xT.dot(y)
    return theta

#test file
inputFile=np.loadtxt("F:\\Coursera Courses\\Machine Learning Course Stan\\Programming Assignments\\PA1\\machine-learning-ex1\\ex1\\ex1data1.txt",delimiter=',')
x=inputFile[:,:1]
#insert the bias weight w0 as 1 in X matrix for regression
X=np.ones((97,2))
X[:,1:]=x
y=inputFile[:,1:]
theta=ols(X,y)
print theta