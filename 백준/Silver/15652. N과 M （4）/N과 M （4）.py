N,M=map(int,input().split())
path=['']*M
used=['']*N

def dfs(level,start):
    if level == M:
        print(*path)
        return
    for i in range(start,N):
        path[level]=i+1
        dfs(level+1,i)


dfs(0,0)