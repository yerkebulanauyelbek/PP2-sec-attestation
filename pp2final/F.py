def power(n):
    if (n==0):
        return False
    while (n!=1):
            if (n%2!=0):
                return False
            n=n//2
    return True
a=list(map(int,input().split()))
a=set(a)
a=sorted(a)
for i in a:
    if power(i):
        a.remove(i)
print(*a)