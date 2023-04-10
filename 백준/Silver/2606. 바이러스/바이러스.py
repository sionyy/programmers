import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
adj=[[] for _ in range(N+1)]
for i in range(M):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)


def dfs(n):
    if visit[n]==1:
        return
    ans.append(n)
    visit[n]=1
    for i in adj[n]:
        dfs(i)


visit=[0]*(N+1)
ans=[]
dfs(1)
print(len(ans)-1)
