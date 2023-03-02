# 횟수
# x,y,너비,높이
N=int(input())
arr = [[0]*1001 for _ in range(1001)]
for k in range(N): #y,x/i,j위치 바꿈
    x, y, m, n = map(int, input().split())
    for i in range(y,y+n):
        for j in range(x,x+m):
            arr[i][j]=k+1

result=[0]*(N+1)
for i in range(1001):
    for j in range(1001):
        if arr[i][j]:
            result[arr[i][j]]+=1

for i in range(1,N+1):
    print(result[i])