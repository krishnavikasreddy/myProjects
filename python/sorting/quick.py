


def QuickSort(num,low,high):
    if(low<high):
        num,index=partition(num,low,high)
        num=QuickSort(num,0,index-1)
        num=QuickSort(num,index+1,high)
    return num

def partition(num,low,high):
    print num
    print "_____"
    pivot=num[low]
    i=low

    for j in range(low+1,high+1):
        if num[j]<pivot:
            temp=num[j]
            num[j]=num[i]
            num[i]=temp
            i=i+1
            print num
            print "___"

    print num,i
    return num,i

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

n=[5,6,3,4,0]
print partition(n,0,len(n)-1)



        
    
