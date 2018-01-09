# -*- coding: utf-8 -*-



import random

with open("KargerMinCut.txt", 'r') as f:
    data = f.readlines()
    graph = {}
    
    for lines in data:
        lines = lines.strip().split('\t')
        graph[int(lines[0])] = [int(x) for x in lines[1:]]
    
#a = {1: [2,3,4], 2: [1,5,4], 3:[1,5], 4:[1,2,5], 5:[2,3,4]}

def contractGraph(graph,ver1, ver2):
    ver2List = [n for n in graph[ver2] if n != ver1]
    
    for n in ver2List:
    	graph[ver1].append(n)
   
    graph.pop(ver2, None)
    
    for n in graph:
        if n == ver1:
            graph[n] = [x for x in graph[n] if x != ver2]
        else:
            graph[n] = [ver1 if x == ver2 else x for x in graph[n]]
    
    return graph


def minCut(graph):
    while len(graph) >2:
        ver1 = random.choice(graph.keys())
        ver2 = random.choice(graph[ver1])
        graph = contractGraph(graph,ver1,ver2)
    return len(graph[graph.keys()[0]])



graphcopy = graph.copy()
min = minCut(graphcopy)
for i in range(400):
    graphcopy = graph.copy()
    x = minCut(graphcopy)
    if(x < min):
        min = x