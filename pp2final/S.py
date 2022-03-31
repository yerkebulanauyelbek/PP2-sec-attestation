n=int(input())
a=list(map(int,input().split()))
c=max(a)
for i in a:
    if i==c:
        print(1,end=" ")
    else:
        print(0,end=" ")