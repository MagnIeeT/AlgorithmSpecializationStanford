
with open("IntegerArray.txt") as f:
    array =[]
    for line in f:
        array.append(int(line))
        
def inversionCount(array):
    lengthArray = len(array)
    if lengthArray == 1:
        return (0,array)
    else:
        count1, A = inversionCount(array[:lengthArray/2])
        count2, B = inversionCount(array[lengthArray/2:])
        
        i = 0;
        j = 0;
        
        C = []
        count3 = 0
        for k in range(lengthArray):
            if ((i < len(A)) and (j<len(B))):
                if (A[i] <= B[j]):
                    C.append(A[i])
                    i +=1
                else:
                    C.append(B[j])
                    j +=1
                    count3 += len(A)-i                    
            elif(j < len(B)):
                C.append(B[j])
                j +=1
            elif(i < len(A)):
                C.append(A[i])
                i +=1
                
        return (count3+count2+count1,C)
        
a, sortedarray = inversionCount(array)        
#2407905288