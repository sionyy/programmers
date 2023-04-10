from collections import deque
import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)
for i in range(N+1):
    adj[i].sort()

def dfs(n):
    ans_dfs.append(n)
    visit[n]=1
    for i in adj[n]:
        if visit[i]==0:
            dfs(i)

def bfs(n):
    q=deque()
    q.append(n)
    ans_bfs.append(n)
    visit[n]=1

    while q:
        now=q.popleft()
        for i in adj[now]:
            if not visit[i]:
                q.append(i)
                ans_bfs.append(i)
                visit[i]=1


visit = [0]*(N+1)
ans_dfs = []
dfs(V)
print(*ans_dfs)
visit = [0]*(N+1)

ans_bfs=[]
bfs(V)
print(*ans_bfs)