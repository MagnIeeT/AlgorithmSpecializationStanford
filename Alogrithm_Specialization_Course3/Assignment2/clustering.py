# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 22:58:35 2018

@author: Neeraj Agrawal
"""

from operator import itemgetter
from unionFind import UnionFind


def main():
    with open("clustering1.txt", 'r') as f:
        data = f.readlines()
        numberNodes = int(data[0])
        
        adjacencyList = []
        
        for line in data[1:]:      
            line = line.split()
            adjacencyList.append([int(line[0]), int(line[1]),int(line[2])])    
            
        adjacencyList = sorted(adjacencyList, key= itemgetter(2),reverse = False)
            
    return adjacencyList, numberNodes

graph, numberNodes = main()

uf = UnionFind(numberNodes)
k= len(set(uf.leaders))
for i in graph:
    if k == 4 and not uf.find(i[0]-1,i[1]-1):
        maxspacing = i[2]
        print maxspacing
        break
    
    if k != 4 and not uf.find(i[0]-1,i[1]-1):
        uf.union(i[0]-1,i[1]-1)
        k= len(set(uf.leaders))
    
        
    
    
    
    