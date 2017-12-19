with open("QuickSort.txt") as f:
    array =[]
    for line in f:
        array.append(int(line))
        
        
def quickSort(array):
    lengthArray = len(array)
    if lengthArray==1:
        return (0,array)
    else:
####### for using last elemnt as pivot##############        
#        dummylast = array[-1]        #for using last element as pivot       
#        array[-1] = array[0]
#        array[0] = dummylast
####################################################      

########Median of Three##########################
        if lengthArray%2 ==0:
            middleindex = lengthArray/2-1
        else:
            middleindex = lengthArray/2
            
        firstele = array[0]
        middleele = array[middleindex]
        lastele = array[-1]
        
        if (((firstele >= middleele) and (firstele < lastele)) or ((firstele <= middleele) and (firstele > lastele))):
            pivotindex = 0
        elif(((middleele > firstele) and (middleele < lastele)) or ((middleele < firstele) and (middleele > lastele))):
            pivotindex = middleindex
        else:
            pivotindex = -1

        dummymedian = array[pivotindex]           
        array[pivotindex] = array[0]
        array[0] = dummymedian            
            


###################################################
                   
        l =0
        pivot = array[l]
        i =l +1
        for j in range(i,lengthArray):
            if array[j] < pivot:
                dummy = array[j]
                array[j] = array[i]
                array[i] = dummy
                i = i+1

        array[l] = array[i-1]
        
        count = 0
        sortArray = []
        if ((i > 1) and (i < lengthArray)):
            count1, lefthalf = quickSort(array[l:i-1])
            sortArray.extend(lefthalf)
            sortArray.append(pivot)
            count2, righthalf = quickSort(array[i:])
            sortArray.extend(righthalf)
            count = count1+ count2 + lengthArray-1
        elif(i==1):
            sortArray.append(pivot)
            count2, righthalf = quickSort(array[i:])
            sortArray.extend(righthalf)
            count = count2 + lengthArray-1
            
        else:
            count1, lefthalf = quickSort(array[l:i-1])
            sortArray.extend(lefthalf)
            sortArray.append(pivot)
            count = count1  + lengthArray -1
        
        
        return (count, sortArray)
             
                
count, sortedArray = quickSort(array)    