N,S=map(int,input().split())
card=list(map(int,input().split()))

cnt=0
path=[0]*N

def dfs(level,start):
    global cnt
    if level>0:
        if sum(path)==S:
            cnt+=1

    if level == N:
        return

    for i in range(start,N):
        path[level]=card[i]
        dfs(level+1,i+1)
        path[level]=0

dfs(0,0)
print(cnt)