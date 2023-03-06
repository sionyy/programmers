T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    
    def boom(y,x):
        summ=0
        for k in range(1,arr[y][x]+1):
            dy=[-k,0,0,k]
            dx=[0,-k,k,0]
            for i in range(4):
                if y+dy[i]>N-1 or x+dx[i]>M-1 or x+dx[i]<0 or y+dy[i]<0:continue
                summ+=arr[y+dy[i]][x+dx[i]]
        return summ+arr[y][x]
    
    MAXX=0
    for i in range(N):
        for j in range(M):
            if MAXX < boom(i,j):
                MAXX = boom(i,j)
    print(f'#{tc} {MAXX}')