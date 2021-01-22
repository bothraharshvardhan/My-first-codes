def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a=0
    b=1
    c=a+b
    s=1
    while(s<=n):
        a=b
        b=c
        c=a+b 
        s=s+1
    return c

print(fibonacci(3))