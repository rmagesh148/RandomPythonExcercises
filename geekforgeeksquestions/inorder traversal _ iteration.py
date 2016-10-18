# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:37:24 2016

@author: MaGesh
"""

class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

def inOrderTraversal(current):
    stack=[]
    done = 0
    while(not done):
        if current is not None:
            stack.append(current)
            current=current.left
        else:
            if(len(stack)>0):
                current=stack.pop()
                print current.data
                current = current.right
            else:
                done =1

root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left=Node(7)
root.left.right.right = Node(8)
inOrderTraversal(root)