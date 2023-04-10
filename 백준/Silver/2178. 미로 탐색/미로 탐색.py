from collections import deque

N,M=map(int,input().split())
arr=[list(map(int,input())) for _ in range(N)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    que=deque()
    que.append((y,x))
    while que:
        y,x=que.popleft()

        for i in range(4):
            ny=dy[i]+y
            nx=dx[i]+x
            if ny<0 or ny>=N or nx<0 or nx>=M:
                continue
            if arr[ny][nx]==0:
                continue
            if arr[ny][nx]==1:
                arr[ny][nx]=arr[y][x]+1
                que.append((ny,nx))
    return arr[N-1][M-1]

print(bfs(0,0))