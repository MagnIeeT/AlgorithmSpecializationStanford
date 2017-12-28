# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:44:36 2017

@author: Neeraj Agrawal
"""

def generateGraph(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        graph = []
        for lines in data:      
            lines = lines.strip().split('\t')        
            graph.append([])
            frm = int(lines[0])
            toNodes = [[int(to.split(',')[0]),int(to.split(',')[1])] for to in lines[1:]]
            graph[frm-1] = toNodes
    return graph

graph = generateGraph("dijkstraData.txt")


explored = [1]
aDist = {}
aDist[1] = 0
     
    
     
while len(explored) < len(graph):
    minWeight = 1000000 
    for nodes in explored:
        for edges in graph[nodes-1]:
            if (edges[0]) not in explored:
                if (edges[1] + aDist[nodes]) < minWeight:
                    minWeight = edges[1] + aDist[nodes]
                    nextAdd = edges[0]
                                
    aDist[nextAdd] = minWeight
    explored.append(nextAdd)
                    
lst = [7,37,59,82,99,115,133,165,188,197]
[aDist[key] for key in lst ]

