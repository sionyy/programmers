from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
arr=[[]for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    arr[b].append(a)

def bfs(n):
    cnt=1
    v=[0]*(N+1)
    q=deque()
    q.append(n)
    v[n]=1

    while q:
        now = q.popleft()
        for i in arr[now]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)
                cnt+=1
    return cnt

ans=[]
for i in range(len(arr)):
    ans.append(bfs(i))
for i in range(len(ans)):
    if max(ans)==ans[i]:
        print(i,end=' ')