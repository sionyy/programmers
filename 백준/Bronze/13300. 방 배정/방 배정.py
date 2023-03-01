# N 학생 수 // K 한방 최대 인원
# 성별 / 학년
# 여0 남1
N,K = map(int,input().split())
W = [0]*7
M = [0]*7

for i in range(N):
    s,y = map(int,input().split())
    if s ==0:
        W[y]+=1
    else:
        M[y]+=1
cnt=0
for i in range(7):
    if W[i] !=0 and W[i] <= K:
        cnt+=1
    elif W[i] >= K and W[i]%K ==0:
        cnt+=W[i]//K
    elif W[i] > K:
        cnt+=W[i]//K+1

for i in range(7):
    if M[i] !=0 and M[i] <= K:
        cnt+=1
    elif M[i] >= K and M[i]%K ==0:
        cnt+=M[i]//K
    elif M[i] > K:
        cnt+=M[i]//K+1

print(cnt)