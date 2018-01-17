# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:49:12 2018

@author: Neeraj
"""

import math
#import matplotlib.pyplot as plt
import numpy as np


def generateGraph(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        numCities = int(data[0])
        graph = []
        for lines in data[1:]:      
            lines = lines.split(' ')     
            graph.append([float(lines[0]),float(lines[1])])
    return graph, numCities



#plt.scatter([x[0] for x in graph],[x[1] for x in graph], )
#DistanceGraph1 = DistanceGraph[0:13]
#DistanceGraph2 = DistanceGraph[11:]


def calculateDistance(graph):
    numCities = len(graph)
    DistanceGraph = []  
    for i in range(numCities):
        DistanceGraph.append([])
        for j in range(numCities):
            DistanceGraph[i].append(math.sqrt((graph[i][0] - graph[j][0])**2 + (graph[i][1] - graph[j][1])**2 ))
    return DistanceGraph
               

def createSets(numCities):
    sets = {}
    for i in range(numCities):
        sets[i] = []
    for i in range(2**(numCities-1)):
        sets[bin(i).count('1')].append(i)        
    return sets
    
   

def onesIndices(num):
    onesIndices = []
    bl = num.bit_length()
    for i in range(bl):
        if num & 0b1 == 1:
            onesIndices.append(i+1)
        num = num >> 1
    return onesIndices



def tsp(graph,distance):
    numCities = len(graph)
    sets = createSets(numCities)
    A = np.ones((2**(numCities-1), numCities), dtype='float')
    A = A*float('inf')
    A[0,0] = 0 
    
    
    for m in range(1, numCities):
        for setElement in sets[m]:
            jS = onesIndices(setElement)
            jS1 = [0] +jS 
            for j in jS:
                xorMask = 2**(j-1)
                previousSet = setElement ^ xorMask                
                minValue = float('inf')

                for k in jS1:
                    if k !=j:
                        val = A[previousSet, k] + distance[k][j]
                        minValue = val if val < minValue else minValue
                        
                A[setElement,j] = minValue
            
    shortestRoute = float('inf')
    for j in range(1, numCities):
        val = A[2**(numCities-1)-1, j] + distance[j][0]
        shortestRoute = val if val < shortestRoute else shortestRoute  
            
    return A, shortestRoute
    
graph, numCities = generateGraph("tsp.txt")
graph1 = graph[:13]
graph2 = graph[11:]

distance1 =calculateDistance(graph1)
A1, shortestRoute1 = tsp(graph1,distance1)

distance2 =calculateDistance(graph2)
A2, shortestRoute2 = tsp(graph2,distance2)    

shortestDistance = shortestRoute1 + shortestRoute2  - 2*distance2[0][1]

     
     
     
     
     
     
     


