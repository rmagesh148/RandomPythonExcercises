# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:56:46 2016

@author: MaGesh
"""

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key

def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+1+size(node.right))

root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left=Node(7)
root.left.right.right = Node(8)
print size(root)