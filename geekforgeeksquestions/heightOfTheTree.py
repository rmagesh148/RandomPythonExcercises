# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:52:10 2016

@author: MaGesh
"""

class Node:
    def __init__(self,key):
        self.left= None
        self.right = None
        self.data = key

def height(node):
    if node is None:
        return 0

    lDepth = height(node.left)
    rDepth = height(node.right)
        
    if (lDepth>rDepth):
        return lDepth+1
    else:
        return rDepth+1

root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left=Node(7)
root.left.right.right = Node(8)
print height(root)