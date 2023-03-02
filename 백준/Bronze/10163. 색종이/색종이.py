# 횟수
# x,y,너비,높이
N=int(input())
arr = [[0]*101 for _ in range(101)]

for k in range(N): #y,x가 일반적이지만 반대여서 i,j위치 바꿈
    x, y, m, n = map(int, input().split())
    for j in range(m):
        for i in range(n):
            arr[y+i][x+j]=k+1 #더하는게 아니라 =으로 할당해야함

full=[]
for i in range(len(arr)): #arr을 1차원 배열로 만들기
    full+=arr[i]          # == conunt 쉽게 하기 위해서

cnt=0
result=[]
for j in range(1,N+1): #count 1부터 N까지를 출력하기
    print(full.count(j))

