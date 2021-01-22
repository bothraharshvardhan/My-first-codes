def sum(a,n):
    s=0
    for i in range(0,n):
       s=s+a[i]
    print(s) 

def allsums(a):
    for i in range(0,len(a)):
        s=0
        for j in range(0,i+1):
            "sum(a,len(a)-i)"
            s=s+a[j]
        print(s)
            


a=[7,-1,2,4]
allsums(a)
