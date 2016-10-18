# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:08:58 2016

@author: MaGesh
"""

class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

def printAncestors(root,key):
    if root is None:
        return False
    if root.data == key:
        return True 
    
    if (printAncestors(root.left,key) or printAncestors(root.right,key)):
        print root.data
        return True

root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left=Node(7)
root.left.right.right = Node(8)
printAncestors(root,8)