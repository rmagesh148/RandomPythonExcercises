# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:22:13 2016

@author: MaGesh
"""

class Node:
    def __init__(self,key):
        self.left= None
        self.right = None
        self.data = key

#function to print Inorder traversal
def printInOrder(root):
    
    if root:
        
        printInOrder(root.left)
        
        print(root.data)
        
        printInOrder(root.right)
        
def printPostOrder(root):
    
    if root:
        
        printPostOrder(root.right)
        
        printPostOrder(root.left)
        
        print(root.data)
        
def printPreOrder(root):
    
    if root:
        
        print(root.data)        
        
        printPreOrder(root.left)
        
        printPreOrder(root.right)
        
        


root = Node(1)

root.left = Node(2)
root.right= Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

printInOrder(root)
print " "
printPreOrder(root)
print " "
printPostOrder(root)