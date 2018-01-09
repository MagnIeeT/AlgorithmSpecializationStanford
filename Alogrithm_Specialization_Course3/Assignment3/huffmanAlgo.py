# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 12:11:02 2018

@author: Neeraj Agrawal

"""


import heapq


class Node:
    def __init__(self,weight,nameNode = None,left=None,right=None):
        self.left = left
        self.right = right
        self.weight = weight
        self.nameNode = nameNode
        
    def getChildren(self):
        return(self.left,self.right)
    
    def __repr__(self):
        return "%s-%s-%s_%s" % (self.nameNode,self.weight,self.left,self.right)
    
    def __cmp__(self,a):
        return cmp(self.weight,a.weight)
        
        


def graph():
    with open("huffman.txt", 'r') as f:
        data = f.readlines()
        numberSymbol = int(data[0])
        
        weightList =[]
        i = 1
        for line in data[1:]: 
            weightList.append(Node(int(line),nameNode = str(i)))
            i=i+1
                    
    return numberSymbol ,weightList


numberSymbol, weightList = graph()
heapq.heapify(weightList)


while len(weightList) >1:
    l = heapq.heappop(weightList)
    r = heapq.heappop(weightList)
    n = Node(l.weight+r.weight,None,l,r)
    heapq.heappush(weightList,n)


codes = {}

def codeIt(s, node):
	if node.nameNode:
		if not s:
			codes[node.nameNode] = "0"
		else:
			codes[node.nameNode] = s
	else:
		codeIt(s+"0", node.left)
		codeIt(s+"1", node.right)

codeIt("",weightList[0])

maxlength = 0
minlength = 10000
for values in codes.values():
    if len(values) > maxlength:
        maxlength = len(values)
    if len(values) < minlength:
        minlength = len(values)




