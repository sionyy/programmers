N,M=map(int,input().split())

card=list(map(int,input().split()))
card.sort()


used=[0]*N
path=[0]*M
def dfs(level):
    if level == M:
        print(*path)
        return

    for i in range(len(card)):
        if used[i]==1:
            continue
        used[i]=1
        path[level]=card[i]
        dfs(level+1)
        used[i]=0

dfs(0)