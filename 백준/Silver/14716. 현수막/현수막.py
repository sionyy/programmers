from collections import deque
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

ny=[-1,-1,-1,0,0,1,1,1]
nx=[-1,0,1,-1,1,-1,0,1]
visit=[[0]*M for _ in range(N)]

def bfs(y,x):
    q=deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(8):
            dy=ny[i]+y
            dx=nx[i]+x
            if dy<0 or dx<0 or dy>=N or dx>=M:
                continue
            if arr[dy][dx]==1 and visit[dy][dx]==0:
                visit[dy][dx]=1
                q.append((dy,dx))

cnt=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and visit[i][j]==0:
            visit[i][j] = 1
            bfs(i,j)
            cnt+=1
print(cnt)