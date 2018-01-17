# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:51:33 2018

@author: Neeraj Agrawal
"""

with open('g3.txt', 'r') as f:
    data = f.readlines()
    numVert , numEdge = data[0].split(' ')
    graph = []

    for i in range(int(numVert)):
        graph.append([[],[]])
    
    for lines in data[1:]:      
        line = lines.split(' ')   
        frm = int(line[0])
        graph[frm-1][0].append(int(line[1])-1)
        graph[frm-1][1].append(int(line[2]))
        
        
numVert = int(numVert)

A = [[[0]*2 for i in range(numVert)] for j in range(numVert)]

for i in range(numVert):
    for j in range(numVert):
        if i == j:
            A[i][j][0] = 0   
        elif j in graph[i][0]:
            A[i][j][0] = graph[i][1][graph[i][0].index(j)]
        else:
            A[i][j][0] = 100000000 #very large number


            
for k in range(1,numVert+1):
    for i in range(numVert):
        for j in range(numVert):
            A[i][j][1]= min(A[i][j][0], A[i][k-1][0]+ A[k-1][j][0])
            A[i][j][0] = A[i][j][1]
            

    
    
minVal1 = 100000000
minVal2 = 100000000
for i in range(numVert):
    for j in range(numVert):
        if i ==j:
            if A[i][j][1] < minVal1:
                minVal1 = A[i][j][1]
        else:
            if A[i][j][1] < minVal2:
                minVal2 = A[i][j][1]
    
print (minVal1,minVal2)

    
    
    
    
    
    
    