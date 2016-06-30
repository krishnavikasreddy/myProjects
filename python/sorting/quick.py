import random
import time
def QuickSort(num,low,high):
    if(low<high):
        num,index=partition(num,low,high)
        num=QuickSort(num,0,index-1)
        num=QuickSort(num,index+1,high)
    return num

def partition(num,low,high):
    pivot=num[low]
    i=low+1
    for j in range(low+1,high+1):
        if num[j]<pivot:
            temp=num[j]
            num[j]=num[i]
            num[i]=temp
            i=i+1
    temp=num[i-1]
    num[i-1]=pivot
    num[low]=temp
    return num,i-1
        
    
   

"""def partition(num,low,high):
    print "-----"
    print num
    left=[]
    right=[]
    pivot=num[high]
    i=high
    for j in range(low,high):
        if(num[j]>pivot):
            right.append(num[j])
        else:
            left.append(num[j])
    temp=left+[pivot]+right
    print temp
    for j in range(low,high+1):
        num[j]=temp[j]
    print num
    return num,i"""

n=50
num=[random.randrange(n) for x in range(n)]
i1=time.time()
print(QuickSort(num,0,len(num)-1))
print (time.time()-i1)



        
    
