# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 01:22:17 2017

@author: Neeraj Agrawal

"""
import heapq     


with open("Median.txt", 'r') as f:
    data = f.readlines()
    runningData = []
    for lines in data:      
        lines = lines.strip()
        runningData.append(int(lines))
        




H_low =[]
H_high =[]
heapq.heapify(H_low)
heapq.heapify(H_high)

median = []
count1=0
count2=0
for i in range(len(runningData)):
    newele = runningData[i]
    if i >0:

        if newele > abs(heapq.nsmallest(1,H_low)[0]):
             heapq.heappush(H_high,newele)
             count1= count1+1
             
        else:
             heapq.heappush(H_low,newele*-1)
             count2= count2+1
        
        if (i%2!=0) and (count1 != count2):

            if count1 > count2:
                count1 = 0
                count2 = 0
                poppedele = heapq.heappop(H_high)
                heapq.heappush(H_low, poppedele*-1)
            else:
                count1 = 0
                count2 = 0
                poppedele = heapq.heappop(H_low)
                heapq.heappush(H_high, poppedele*-1)
                
        
        if (i %2==0):
            if count1 > count2:
                median.append(heapq.nsmallest(1,H_high)[0])
            else:
                median.append(abs(heapq.nsmallest(1,H_low)[0]))
        else:
            median.append(abs(heapq.nsmallest(1,H_low)[0]))
        
    else:
        heapq.heappush(H_low,newele*-1)
        count2 = count2+1
        median.append(newele)
            
        
    
        


    
    
    
    
    
    