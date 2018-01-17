# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 22:48:14 2018

@author: Neeraj Agrawal
"""


from unionFind import UnionFind

def graph():
    with open("clustering_big.txt", 'r') as f:
        data = f.readlines()
        numberNodes = int(data[0].split()[0])
        
        vertexlist =[]
        
        for line in data[1:]: 
            node = "".join([ el for el in line if el is not " "])[:-1]
            vertexlist.append(node)
                    
    return numberNodes ,list(set(vertexlist))

numberNodes, vertexlist = graph()
hastable ={}
for i,ele in enumerate(vertexlist):
    hastable[ele] = i


uf = UnionFind(len(vertexlist))
        
def generatecloseVertex(vertex):
    newVertices1 = []
    newVertices2 = []
    for i in range(len(vertex)):
        newVertex = (vertex[:i]+str(int(not(int(vertex[i])))) + vertex[i+1:])
        newVertices1.append(newVertex)
        
    for i in range(len(vertex)-1):
        newVertex = (vertex[:i]+str(int(not(int(vertex[i])))) + vertex[i+1:])
        for j in range(i+1, len(vertex)):
            newVertex2 = (newVertex[:j]+str(int(not(int(newVertex[j])))) + newVertex[j+1:])
            newVertices2.append(newVertex2) 
              
    return newVertices1 + newVertices2
    
    
def clustering(hastable,uf, vertexlist):
    for node in vertexlist:
        newVertices = generatecloseVertex(node)
        for closenode in newVertices:
            try:
                uf.union(hastable[closenode],hastable[node])
            except:
                None
                
    k  = len(set(uf.leaders))
    return k
                
print clustering(hastable,uf,vertexlist)  
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    