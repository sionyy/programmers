N,M=map(int,input().split())
card=list(map(int,input().split()))
card.sort()
used=[0]*N
path=[0]*M
lst=[]

def dfs(level,start):
    if level==M:
        lst.append(tuple(path))
        return

    for i in range(start,N):
        if used[i]:
            continue
        used[i]=1
        path[level]=card[i]
        dfs(level+1,i+1)
        used[i]=0

dfs(0,0)
new=sorted(set(lst))

for i in range(len(new)):
    print(*new[i])