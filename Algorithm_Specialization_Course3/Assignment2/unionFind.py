# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 00:23:20 2018

@author:  Neeraj Agrawal
"""

class UnionFind:
    
    def __init__(self, numberNodes):
        self.leaders = list(range(numberNodes))
        self.size = [1]*numberNodes
                                                    
#    def findleader(self,i):
#        return self.leaders[self.leaders[i]]
 
    def findleader(self,i):
        j = i
        while (j != self.leaders[j]):
            self.leaders[j] = self.leaders[self.leaders[j]]
            j = self.leaders[j]
        return j 
    
    
    
    def find(self, p,q):
        return self.findleader(p)== self.findleader(q)
    
    
    def union(self,p,q):
        i = self.findleader(p)
        j = self.findleader(q)
        
        if self.size[i] >= self.size[j]:
            self.leaders[:] = [i if x==self.leaders[j] else x for x in self.leaders]
            self.size[i] += self.size[j]
        else:
            self.leaders[:] = [j if x==self.leaders[i] else x for x in self.leaders]
            self.size[j] += self.size[i]
        
        
            