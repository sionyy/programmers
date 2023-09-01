from collections import deque

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
answer=[[-1]*M for _ in range(N)]
visit=[[0]*M for _ in range(N)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs():
    q=deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i,j))
                visit[i][j]=1
                answer[i][j]=0
            if arr[i][j]==0:
                answer[i][j]=0
    while q:
        y,x = q.popleft()
        for k in range(4):
            ny=dy[k]+y
            nx=dx[k]+x
            if 0<=ny<N and 0<=nx<M:
                if visit[ny][nx]==0 and arr[ny][nx]!=0:
                    visit[ny][nx]=visit[y][x]+1
                    answer[ny][nx]=visit[y][x]
                    q.append((ny,nx))

bfs()
for i in range(N):
    print(*answer[i])