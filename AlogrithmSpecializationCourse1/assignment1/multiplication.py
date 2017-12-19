

def multiplyKaratsuba(x,y):
    if (int(x) <10 or int(y) <10):
        return int(x)*int(y)
    else:
        
        lenX = len(x)
        lenY = len(y)       
        
        maxLength = max(lenX,lenY)
        if (maxLength % 2 != 0):
            maxLength+=1
        while (lenX != maxLength):
            x = "0" + x
            lenX = len(x)
        while (lenY != maxLength):
            y = "0" + y
            lenY= len(y)
            
        a = x[0:lenX/2]
        b = x[lenX/2:]
        c = y[0:lenY/2]
        d = y[lenY/2:]
        
        ac = multiplyKaratsuba(a,c)
        bd = multiplyKaratsuba(b,d)
        adbc = multiplyKaratsuba(str(int(a)+int(b)),str(int(c)+int(d))) - ac - bd
        result = (10**lenX)*ac + (10**(lenX/2))*adbc + bd                  
#        print(x,y,result)
        return result
                                
                                
    
import time
start = time.clock()
multiplyKaratsuba("3141592653589793238462643383279502884197169399375105820974944592","2718281828459045235360287471352662497757247093699959574966967627")
print time.clock() - start   
                
