from collections import deque

F,S,G,U,D=map(int,input().split())
def bfs(s,e):
    q=deque()
    v=[0]*(F+U+1)
    q.append(s)
    v[s]=1

    direct=[U,-D]
    while q :
        now = q.popleft()
        if now == e:
            return v[now]-1

        for i in range(2):
            if v[direct[i]+now]==0 and 0<direct[i]+now<F+1:
                q.append(direct[i]+now)
                v[direct[i]+now]=v[now]+1
    return -1

ans=bfs(S,G)
if ans == -1:
    print("use the stairs")
else:
    print(ans)