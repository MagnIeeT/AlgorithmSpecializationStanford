# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 23:42:19 2018

@author: Neeraj Agrawal
"""


import sys
sys.setrecursionlimit(3000)


def readTable():
    with open("knapsack_big.txt", 'r') as f:
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

A ={}

def knapsackRecursive(value,size, knapsack_size):

    if len(value)==0:
        return 0
    
    try:
        return A[(len(value),knapsack_size)]
    
    except:
        a = knapsackRecursive(value[:-1],size[:-1],knapsack_size)
        if size[-1] < knapsack_size:                     
            c= knapsackRecursive(value[:-1],size[:-1],knapsack_size-size[-1]) 
            A[(len(value),knapsack_size)] = max(value[-1]+c,a)
            return A[(len(value),knapsack_size)] 
        else:               
            A[(len(value),knapsack_size)] = a
            return A[(len(value),knapsack_size)] 
            

knapsackRecursive(value,size,knapsack_size)        
