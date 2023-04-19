"""
건물 F층
현재 S층
목표 G층

위로 U
아래 D

use the stairs
"""

# 3 5 7 9 8 10

F,S,G,U,D=map(int,input().split())
def bfs(s,e):
    q=[]
    v=[0]*(F+U+1)
    q.append(s)
    v[s]=1

    direct=[U,-D]
    while q :
        now = q.pop(0)
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