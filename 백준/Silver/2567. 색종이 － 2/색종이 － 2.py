arr = [[0]*100+[0]*10 for _ in range(110)]

N=int(input())
for k in range(N):
    y,x = map(int,input().split())
    for i in range(10):
        for j in range(10):
            arr[y+i+1][x+j+1]=1

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def check(y,x):
    cnt=0
    rlt=0
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny<0 or nx<0 or ny>109 or nx>109: continue
        if arr[ny][nx] ==1:
            cnt+=1
        # if arr[0][x] ==1 or arr[y][0] ==1:
        #     cnt+=1
    return cnt

ans=0
for i in range(110):
    for j in range(110):
        if arr[i][j]==0:
            ans += check(i, j)
print(ans)
