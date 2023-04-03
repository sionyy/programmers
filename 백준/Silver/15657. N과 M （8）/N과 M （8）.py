N,M=map(int,input().split())

card=list(map(int,input().split()))
card.sort()


used=[0]*N
path=[0]*M
def dfs(level,start):
    if level == M:
        print(*path)
        return

    for i in range(start,len(card)):
        path[level]=card[i]
        dfs(level+1,i)

dfs(0,0)