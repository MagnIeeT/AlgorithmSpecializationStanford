# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:43:17 2018

@author: Neeraj Agrawal
"""

import math   

def generateGraph(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        numCities = int(data[0])
        graph = []
        for lines in data[1:]:      
            lines = lines.split(' ')     
            graph.append([float(lines[0]),float(lines[1]),float(lines[2])])
    return graph, numCities


graph, numCities = generateGraph('nn.txt')
path = [0]
pathDict ={0:True}
for i in range(1,numCities):
    pathDict[i] =False
    
totalDistance = 0.0

for i in range(0,numCities-1):
    minValue = float('inf')    
    for j in range(numCities):
        if not(pathDict[j]):
            dist = (graph[path[i]][1] - graph[j][1])**2 + (graph[path[i]][2] - graph[j][2])**2 
            xDist  = (graph[path[i]][1] - graph[path[i]][1])**2
            if minValue > xDist:
                if dist < minValue:
                    minValue = dist
                    nodetoAdd = j
            else:
                break
            
    totalDistance = totalDistance + math.sqrt(minValue)
    path.append(nodetoAdd)
    pathDict[nodetoAdd] =True
    

totalDistance = totalDistance + math.sqrt((graph[0][1] - graph[path[-1]][1])**2 + (graph[0][2] - graph[path[-1]][2])**2 )
    
    















