N,M=map(int,input().split())
card=list(map(int,input().split()))
card.sort()
path=[0]*M
used=[0]*N
lst=[]

def dfs(level):
    if level == M:
        lst.append(tuple(path))
        return

    for i in range(N):
        path[level]=card[i]
        dfs(level+1)

dfs(0)

new=sorted(set(lst))
for i in range(len(new)):
    print(*new[i])