def power(n):
    if (n==0):
        return False
    while (n!=1):
            if (n%2!=0):
                return False
            n=n//2
    return True
a=list(map(int,input().split()))
b=[]
for i in a:
    if power(i):
        b.append(i)
b=set(b)
b=sorted(b)
print(*b)