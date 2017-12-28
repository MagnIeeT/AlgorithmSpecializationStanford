# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:20:22 2017

@author: Neeraj Agrawal
"""


import threading
import sys
       
        
def hashfunction(keyNumber, size):
    if keyNumber < 0:
        index = (-1*keyNumber)% size
    else:
        index = (keyNumber)% size
    return index
        

class HashTable:

    def __init__(self, capacity=1142287):
        self.capacity = capacity
        self.size = 0
        self.data = [[] for _ in range(capacity)]

    def _find_by_key(self, keyNumber, find_result_func):
        index = hashfunction(keyNumber, self.capacity)
        hash_table_cell = self.data[index]
        found_item = None
        for item in hash_table_cell:
            if item == keyNumber:
                found_item = item
                break

        return find_result_func(found_item, hash_table_cell)

    def set(self, keyNumber):
        
        def find_result_func(found_item, hash_table_cell):
            if found_item:
                None
            else:
                hash_table_cell.append(keyNumber)
                self.size += 1

        self._find_by_key(keyNumber, find_result_func)
        

    def get(self, keyNumber):
        def find_result_func(found_item, _):
            if found_item:
                return found_item
            else:
                False

        return self._find_by_key(keyNumber, find_result_func)
    
#    def remove(self, keyNumber):
#        def find_result_func(found_item, hash_table_cell):
#            if found_item:
#                hash_table_cell.remove(found_item)
#                self.size -= 1
#   
#        return self._find_by_key(keyNumber, find_result_func)
    
    
    
#def main():
#    H = HashTable()
#    with open("algo1-programming_prob-2sum.txt", 'r') as f:
#        data = f.readlines()
#        runningData =[]
#        for lines in data:      
#            lines = lines.strip()
#            H.set(int(lines))
#            runningData.append(int(lines))
#            
#    count =0
#    for j in range(-10000,10001):
#        for i in runningData:
#            if i != (j-i):
#                if H.get(j-i):
#                    count +=1 
#                    break
#    print count


def main():
    H = {}
    with open("algo1-programming_prob-2sum.txt", 'r') as f:
        data = f.readlines()
        runningData =[]
        for lines in data:      
            lines = lines.strip()
            H[int(lines)]=True
            runningData.append(int(lines))
            
    count =0
    for j in range(-10000,10001):
        for i in runningData:
            if (j-i) in H and i != (j-i):
                count +=1 
                break
    print count

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
    
#427