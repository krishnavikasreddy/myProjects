import random
import time

def mergesort(num):
    if len(num)>1:
        index=int(round(len(num)/2))
        left= mergesort(num[:index])
        right= mergesort(num[index:])
        return merge(left,right)
    else:
        return num

def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]>=right[j]:
            result.append(right[j])
            j=j+1
        else:
            result.append(left[i])
            i=i+1
    if i<len(left):
        result=result+left[i:]
    elif j<len(left):
        result=result+right[j:]
    return result
        
 
def insertion(num):
    for j in range(1,len(num)):
        i=j-1
        key=num[j]
        while i>=0 and num[i]>key:
            num[i+1]=num[i]
            i=i-1
        num[i+1]=key
    return num
        



n=10000
num=[random.randrange(n) for x in range(n)]
i1=time.time()
mergesort(num)
print time.time()-i1

i1=time.time()
insertion(num)
print time.time()-i1

