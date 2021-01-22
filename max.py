def maximum(a,b,c):
    if a>=b and a>=c:
        return a
    else:
        if b>=c:
            return b
        else:
            return c



import sys
i=1
a=[]
while (int(sys.argv[i]) !=-1):
    a.append(int(sys.argv[i]))
    i=i+1

for i in range(len(a)-1,-1,-1):
    print(a[i])
