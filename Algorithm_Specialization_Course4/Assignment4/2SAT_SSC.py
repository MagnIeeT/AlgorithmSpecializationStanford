# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:13:15 2018

@author: Neeraj Agrawal
"""

def createGraph(fName):
    edgeList = []

    with open(fName) as f:
        data = f.readlines()
        numVars = numClauses = int(data[0].strip())
        for line in data[1:]:
            vert1, vert2 = [ int(el) for el in line.split() ]
            edgeList.append(([-vert1, vert2]))
            edgeList.append(([-vert2, vert1]))

    return edgeList, numVars, numClauses



def adjacencyList(edgeList):
    graph = {}
    graph_reversed ={}
    vertexSet = set()
           
    for vert1,vert2 in edgeList:  
        

        if vert1 not in vertexSet:
            vertexSet.add(vert1)
        if vert2 not in vertexSet:
            vertexSet.add(vert2)

        if vert1 not in graph:
            graph[vert1] = [vert2]
        else:
            graph[vert1].append(vert2)
            
        if vert2 not in graph_reversed:
            graph_reversed[vert2] = [vert1]   
        else:
            graph_reversed[vert2].append(vert1)
            
                   
    return graph, graph_reversed, vertexSet



def dfs_loop1(graph,vertexSet):
    
    global explored
    global finishingTime
    global t 
    
    for key in vertexSet:
        explored[key] =False
    
    for i in reversed(graph.keys()):
        if not explored[i]:
            dfs1(graph, i)
    return None
            
            
def dfs1(graph, node):
    global t
    explored[node] = True
    
    if node in graph:
        for j in graph[node]:
            if not explored[j]:
                dfs1(graph,j)
    t = t+ 1
    finishingTime[node] = t
    return None
                

def dfs_loop2(graph, vertexSet):
    global explored2
    global leaders
    global finishingTime2
    
    for key in vertexSet:
        explored2[key] =False
    
    finishingTime2 ={y:x for x,y in finishingTime.iteritems()}
    
    for i in reversed(finishingTime2.keys()):
        node = finishingTime2[i]
        if not explored2[node]:
            dfs2(graph,node,node)
            
    return None

def dfs2(graph,node,source):
    
    leaders[node]=source
    explored2[node]=True
             
    if node in graph:        
        for j in graph[node]:
            if not explored2[j]:
                dfs2(graph, j, source)
    return None
        

def kosarajuCount(graph,graph_reversed,vertexSet):
    dfs_loop1(graph_reversed,vertexSet)
    dfs_loop2(graph,vertexSet) 
    return None


def main(filename):  
    
    print ("Reading File...")
    edgeList, numVars, numClauses = createGraph(filename)
    print("Creating AdjacenyList...")
    graph, graph_reversed, vertexSet = adjacencyList(edgeList)
    print("Finding leaders of SCC...")
    kosarajuCount(graph,graph_reversed,vertexSet)
    
    print("Checking Satisfiability...")
    success =1
    for vertex in range(1, numVars+1):
        if vertex in leaders and -vertex in leaders:
            if leaders[vertex] == leaders[-vertex]:
                success = 0
                break
    
    
    if success ==1:
        print "Satisfiable"
    else:
        print "Unsatisfiable"

#####Global Variable
explored ={}
finishingTime ={}
t =0
explored2 ={}
leaders ={}

main("2sat6.txt")








    