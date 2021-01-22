def bubblesort(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
    return a

def getMin(a,start):
    v=[a[start],start]
    for i in range(start+1,len(a)):
        if a[i]<v[0]:
            v[0]=a[i]
            v[1]=i
    return v
def selectionsort(a):
    for i in range(0,len(a)-1):
        m=getMin(a,i+1)
        if(a[i]>m[0]):
            c=a[i]
            a[i]=a[m[1]]
            a[m[1]]=c
            

def search(a,n):
    for i in range(0,len(a)):
        if(a[i]==n):
            return 1
    return 0
        
def binarySearch(a,n,start,end):
    #pivot=int(len(a)/2)
    if end<0:
        return 0
    pivot=start+int((end-start+1)/2)
    if(a[pivot]==n):
        return 1
    if start==end:
        return 0
    if (n<a[pivot]):
        return binarySearch(a,n,start,pivot-1)
    else:
        return binarySearch(a,n,pivot+1,end)
       

def iterativeBinarySearch(a,n):
    start=0
    end=len(a)-1
    
    while(start<=end):
        pivot=start+int((end-start+1)/2)
        if a[pivot]==n:
            return 1
        if n<a[pivot]:
            end=pivot-1
        else:
            start=pivot+1                    
    return 0;

# a is a sorted array
#b is a sorted array
# return a sorted array that merges a and b
def merge(a,b):
    

    
 
import sys
#b=[56,78,92,100,120,130,150,200]
a=[200,120,130,92,100,56,78,150]
b=bubblesort(a)
print(b)
n=int(sys.argv[1])
print("Binary Search: ",binarySearch(b,n,0,len(a)-1))
print("Iterative Binary Search: ",iterativeBinarySearch(b,n))
print("Linear Search: ",search(b,n))




