import random
import time
import math,sys

def mergesort(num,x):
    if len(num)>1:
        index=int(round(len(num)/2))
        left= mergesort(num[:index],x)
        right= mergesort(num[index:],x)
        return merge(left,right,x)
    else:
        return num

def merge(left,right,x):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i][x]>=right[j][x]:
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

def closestPair(points,low,high):
    if low+3<high:
        index=int((low+high)/2)
        dleft,pair1=closestPair(points,low,index)
        dright,pair2=closestPair(points,index,high)
        if dleft<=dright:
            delta=dleft
            pair=pair1
        else:
            delta=dright
            pair=pair2
        return closestPairUn(points,low,high,delta,pair)
    else:
        d=sys.maxint
        pair=[]
        for i in range(low,high):
            for j in range(i+1,high):
                if d>distance(points[i],points[j]):
                    d=distance(points[i],points[j])
                    pair.append(points[i])
                    pair.append(points[j])
                    
        return d,pair
       
            
def closestPairUn(points,low,high,delta,pair):
    index=int((low+high)/2)
    points_near=[]
    for i in range(low,high):
        if (abs(points[index][0]-points[i][0]))<=delta:
            points_near.append(points[i])
    for i in range(0,len(points)):
        for j in range(i+1,min(7,len(points))):
            if delta>distance(points[i],points[j]):
                delta=distance(points[i],points[j])
                pair=[points[i],points[j]]
    return delta,pair
            
    

def distance(x,y):
    return int(math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2)))


points=mergesort([(7, 12), (-2, 3), (3, 4),(7,10),(7,9)],0)
print closestPair(points,0,len(points))
