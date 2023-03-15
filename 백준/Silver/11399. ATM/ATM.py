N=int(input())
lst=list(map(int,input().split()))
lst.sort()
repeat=0
now=0
getsum=0
while repeat<N:
    now+=lst[repeat]
    getsum+=now
    repeat+=1
print(getsum)