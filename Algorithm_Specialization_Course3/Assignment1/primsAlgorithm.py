# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 22:23:02 2018

@author: Neeraj Agrawal
"""



def main():
    with open("edges.txt", 'r') as f:
        data = f.readlines()
        numberNodes = int(data[0].split()[0])
        numberEdges = int(data[0].split()[1])
        
        adjacencyList = []
        for i in range(numberNodes):
            adjacencyList.append([])
        
        for line in data[1:]:      
            line = line.split()
            adjacencyList[int(line[0])-1].append([int(line[1]), int(line[2])])    
            adjacencyList[int(line[1])-1].append([int(line[0]), int(line[2])])
            
    return adjacencyList, numberNodes,numberEdges

graph,numberNodes,numberEdges = main()

X = [1]
overallCost = 0

while len(X) < numberNodes:
    minEdge = 10000000
    for nodes in X:
        for edges in graph[nodes-1]:
            if edges[0] not in X:
                if edges[1] < minEdge:
                    minEdge = edges[1]
                    nextVertex = edges[0]
                    Cost = edges[1]
                    
    X.append(nextVertex)
    overallCost = overallCost +Cost 
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    