N,M=map(int,input().split())
card=list(map(int,input().split()))
lst = sorted(set(card))
path=[0]*M
used=[0]*N

def dfs(level,start):
    if level == M:
        print(*path)
        return
    for i in range(start,len(lst)):
        path[level]=lst[i]
        dfs(level+1,i)

dfs(0,0)