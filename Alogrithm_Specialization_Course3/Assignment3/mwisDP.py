# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 15:22:31 2018

@author: Neeraj Agrawal
"""


def graph():
    with open("mwis.txt", 'r') as f:
        data = f.readlines()
        numberNodes = int(data[0])
        
        vertexWeight =[]
        
        for line in data[1:]: 
            vertexWeight.append(int(line))
                    
    return numberNodes ,vertexWeight

numberNodes, vertexWeight = graph()



A = [0,vertexWeight[0]]
for i in range(2,len(vertexWeight)+1):
    A.append(max(A[i-1],A[i-2]+vertexWeight[i-1]))    

S = []
i = len(A)-1
while i >= 1:
    if A[i-1] >= A[i-2]+vertexWeight[i-1]:
        i = i-1
    else:
        S.append(i)
        i = i-2
        
string =""
for i in [1,2,3,4,17,117,517,997]:
    if i in S:
        string = string + "1"
    else:
        string = string +"0"
        