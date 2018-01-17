# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 20:56:53 2018

@author: Neeraj Agrawal
"""

def readTable():
    with open("knapsack1.txt", 'r') as f:
        data = f.readlines()
        
        knapsack_size = int(data[0].split()[0])
        value = []
        size = []
        
        for line in data[1:]:      
            line = line.split()
            value.append(int(line[0])) 
            size.append(int(line[1]))

            
    return value, size,knapsack_size

value, size, knapsack_size  = readTable()

A = []
for i in range(len(value)+1):
    A.append([])
for j in range(len(value)+1):    
    for i in range(knapsack_size+1):
        A[j].append(0)
    
    
for i in range(1, len(value)+1):
    for x in range(knapsack_size+1):
        if x- size[i-1] < 0:
            A[i][x] = A[i-1][x]
        else:
            A[i][x] = max(A[i-1][x], A[i-1][x -size[i-1]] + value[i-1])
            
        
A[len(value)][knapsack_size]    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    