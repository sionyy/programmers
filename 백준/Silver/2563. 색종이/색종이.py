lst = [[0]*100 for _ in range(100)]

N = int(input())
for i in range(N):
    y,x=map(int,input().split())
    for k in range(y,y+10):
        for t in range(x,x+10):
            lst[k][t]=1

result=0
for i in range(100):
    for j in range(100):
        if lst[i][j] ==1:
            result+=1

print(result)