# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:39:05 2016

@author: MaGesh
"""

class Node:
    def __init__(self,key):
        self.data=key
        self.child=[]

def printLevelTree(root):
    if root is None:
        return 
    queue=[]
    queue.append(root)
    
    while(len(queue)>0):
        n=len(queue)
        while(n>0):
            p = queue[0]
            queue.pop(0)
            print p.data
            for index, value in enumerate(p.child):
                queue.append(value)
            n -= 1
        print " "

root = Node(10)
root.child.append(Node(2))
root.child.append(Node(34))
root.child.append(Node(56))
root.child.append(Node(100))
root.child[2].child.append(Node(1))
root.child[3].child.append(Node(7))
root.child[3].child.append(Node(8))
root.child[3].child.append(Node(9))
printLevelTree(root)
