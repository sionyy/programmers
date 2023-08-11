from collections import deque
N=int(input())
arr=[list(map(int,input())) for _ in range(N)]
ans=[]

def dfs(y,x):
    global cnt
    if y<0 or x<0 or y>=N or x>=N:
        return
    if arr[y][x]==1:
        cnt+=1
        arr[y][x]=0
        dfs(y+1,x)
        dfs(y-1,x)
        dfs(y,x-1)
        dfs(y,x+1)


for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt=0
            dfs(i,j)
            ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)