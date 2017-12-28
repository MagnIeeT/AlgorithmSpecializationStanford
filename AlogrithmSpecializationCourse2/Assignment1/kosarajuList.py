# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:45:06 2017

@author: H213139
"""

import threading
import sys
import os
os.chdir("C:\\Users\\H213139\\Downloads\\Deeplearning\\Algorithm\\AlogrithmAssignmentOrig\\Course2\\Assignment1")
            
def generateGraph(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        graph = []
        graph_reversed =[]
           
        for lines in data:      
            if lines != '\n':
                lines = lines.strip().split(' ')
                while len(graph) < max(int(lines[0]),int(lines[1])):
                    graph.append([])
                    graph_reversed.append([])
                graph[int(lines[0])-1].append(int(lines[1])-1)
                graph_reversed[int(lines[1])-1].append(int(lines[0])-1)
    return graph, graph_reversed


explored =[]
finishingTime ={}
t =0
explored2 =[]
leaderCount ={}


def dfs_loop1(graph):
    
    global explored
    global finishingTime
    global t 
    
    explored = [False]*len(graph)
    for i in reversed(range(len(graph))):
        if not explored[i]:
            dfs1(graph, i)
    return None
            
            
def dfs1(graph, node):
    global t
    explored[node] = True
    
    for j in graph[node]:
        if not explored[j]:
            dfs1(graph,j)
    t = t+ 1
    finishingTime[node] = t
    return None
                

def dfs_loop2(graph):
    global explored2
    global leaderCount
    
    explored2 = [False]*len(graph)
    
    finishingTime2 ={y:x for x,y in finishingTime.iteritems()}
    
    for i in range(len(finishingTime2.keys()),0,-1):
        node = finishingTime2[i]
        if not explored2[node]:
            count = 1
            count = dfs2(graph,node,count)
            leaderCount[i]=count
            
    return None

def dfs2(graph,node,count):
    explored2[node]=True
    for j in graph[node]:
        if not explored2[j]:
            count = count +1
            count = dfs2(graph, j, count)
    return count
        

def kosarajuCount(graph,graph_reversed):

    dfs_loop1(graph_reversed)
    dfs_loop2(graph)    
    finalcount = leaderCount.values()
    finalcount.sort(reverse=True)
    return finalcount
    

def main():
    graph, graph_reversed = generateGraph('SCC.txt')
    finalCount = kosarajuCount(graph, graph_reversed)
    if len(finalCount) > 4:
        print(finalCount[0:5])
    else:
        print(finalCount)



if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
    
#261,231,214,196,185