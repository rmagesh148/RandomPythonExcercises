# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:49:44 2016

@author: MaGesh
"""

class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

def printLevelOrder(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        print queue[0].data
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
            
            
root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left=Node(7)
root.left.right.right = Node(8)
printLevelOrder(root)
        