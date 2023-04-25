from collections import deque
import sys
input = sys.stdin.readline

N,M,K,X=map(int,input().split())

check=[0]*(N+1)
v=[0]*(N+1)
arr=[[] for _ in range(N+1)]

for i in range(M):
    st,ed=map(int,input().split())
    arr[st].append(ed)

def bfs(n):
    q=deque()
    q.append(n)

    while q:
        now = q.popleft()
        v[now]=1
        for i in arr[now]:
            if v[i]==0:
                q.append(i)
                check[i]=check[now]+1
                v[i]=1
bfs(X)

ans=[]
for i in range(len(check)):
    if check[i] == K:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)