import sys
input=sys.stdin.readline
N=int(input())
lst=[]
for i in range(N):
    st,ed=map(int,input().split())
    lst.append([st,ed])

lst.sort(key=lambda x:x[1])
for i in range(N):
    if lst[i][0]==lst[i][1]:
        for j in range(i+1,N):
            if lst[i] !=lst[j] and lst[i][1] == lst[j][1]:
                lst[i],lst[j]=lst[j],lst[i]
# print(lst)

start=-1
ans=0
for i in range(N):
    if lst[i][0]>=start:
        start=lst[i][1]
        ans+=1
    elif lst[i][0] == lst[i][1]:
        ans += 1
print(ans)
