L,M=map(int,input().split())
lst=input().split()

path=[0]*L
ans=[]
def dfs(start,level):
    if level == L:
        cnt=0
        if ('a' in path) or ('e' in path) or ('i' in path) or ('o' in path) or ('u' in path):
            for i in range(len(path)):
                if path[i] == 'a' or path[i] == 'e' or path[i] =='i' or path[i] =='o' or path[i]=='u':
                    cnt+=1
            if cnt>L//2:
                return
            ans.append(sorted(path))
            return
        else:
            return

    for i in range(start,M):
        path[level]=lst[i]
        dfs(i+1,level+1)
dfs(0,0)


ans.sort()
for i in range(len(ans)):
    print(''.join(ans[i]))