H,W = map(int,input().split())
arr = [list(input()) for _ in range(H)]
ans = [['.']*W for _ in range(H)]
for i in range(H):
      for j in range(W):
            if arr[i][j]=='c':
                  ans[i][j]=0

for i in range(H):
      cnt = 0
      for j in range(W):
            if ans[i][j] == 0:
                  cnt=0
            if ans[i][j] =='.':
                  cnt+=1
                  ans[i][j] = cnt

for i in range(H):
      if ans[i].count(0) == 0:
            for j in range(W):
                  ans[i][j] = -1

      for j in range(W):
            if ans[i][j] == 0:
                  for k in range(j-1,-1,-1):
                        ans[i][k] = -1
                  break

for i in range(H):
      print(*ans[i])

