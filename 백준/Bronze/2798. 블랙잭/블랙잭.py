# 카드개수 N // 최대합 M
N,M=map(int,input().split())
lst = list(map(int,input().split()))
result=[]

for i in range(N-2):
    summ = 0
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            summ=lst[i]+lst[j]+lst[k]
            result.append(summ)
result.sort()

ans=0
if len(result) == 1:
    ans=result[0]
else:
    for i in range(len(result)):
        if M < result[i]:
            ans =result[i-1]
            break
        else:
            ans=result[-1]
print(ans)