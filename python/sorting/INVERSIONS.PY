import random
import time

def mergesort(num):
    if len(num)>1:
        index=int(round(len(num)/2))
        left= mergesort(num[:index])
        right= mergesort(num[index:])
        return sort_and_count(left,right),inv
    else:
        return num,0

def sort_and_count(left,right):
    result=[]
    i=0
    j=0
    inv=0
    while i<len(left) and j<len(right):
        if left[i]>=right[j]:
            result.append(right[j])
            j=j+1
            inv=inv+len(left)-i
        else:
            result.append(left[i])
            i=i+1
    if i<len(left):
        result=result+left[i:]
    elif j<len(left):
        result=result+right[j:]
    return result,inv

num