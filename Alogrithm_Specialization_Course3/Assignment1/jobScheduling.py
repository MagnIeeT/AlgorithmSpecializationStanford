# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 18:56:15 2018

@author: Neeraj Agrawal
"""

from operator import itemgetter


def main1():
    with open("jobs.txt", 'r') as f:
        data = f.readlines()
        runningData =[]
        for lines in data[1:]:      
            lines = lines.split()
            runningData.append([int(lines[0]),int(lines[1]), int(lines[0])-int(lines[1])])
        
        runningData = sorted(runningData, key= itemgetter(0),reverse = True)
        runningData = sorted(runningData, key= itemgetter(2),reverse = True)
    
    
    completionTime =0
    weightedSum = 0
    for ele in runningData:
        completionTime = completionTime + ele[1]
        weightedSum = weightedSum + completionTime*ele[0]    
    
    return weightedSum
            
weightedSum1 = main1()


def main2():
    with open("jobs.txt", 'r') as f:
        data = f.readlines()
        runningData =[]
        for lines in data[1:]:      
            lines = lines.split()
            runningData.append([int(lines[0]),int(lines[1]), float(lines[0])/float(lines[1])])
        
        runningData = sorted(runningData, key= itemgetter(2),reverse = True)
    
    
    completionTime =0
    weightedSum = 0
    for ele in runningData:
        completionTime = completionTime + ele[1]
        weightedSum = weightedSum + completionTime*ele[0]    
    
    return weightedSum
            
weightedSum2 = main2()
