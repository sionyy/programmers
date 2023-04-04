def dfs(start,level,lst):
    if level ==6:
        print(*path)
        return

    for i in range(start,len(lst)):
        path[level]=lst[i]
        dfs(i+1,level+1,lst)

temp=['temp']
while True:
    temp=list(map(int,input().split()))
    if temp[0]==0:
        break

    num=temp[0]
    card=sorted(temp[1:])
    path=[0]*6
    dfs(0,0,card)
    print()