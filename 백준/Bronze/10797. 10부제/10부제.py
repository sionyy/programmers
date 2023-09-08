N=int(input())
lst=list(map(int,input().split()))
ans=0
for i in range(len(lst)):
    if lst[i]==N:
        ans+=1
print(ans)