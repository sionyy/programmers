# N 학생 수 // K 한방 최대 인원
# 성별 / 학년
# 여0 남1
N,K = map(int,input().split())
M1,M2,M3,M4,M5,M6 = [],[],[],[],[],[]
W1,W2,W3,W4,W5,W6 = [],[],[],[],[],[]
school = [M1,M2,M3,M4,M5,M6,W1,W2,W3,W4,W5,W6]
for i in range(N):
    gen,grade = map(int,input().split())
    if gen ==0 and grade == 1:
        M1.append(1)
    elif gen ==0 and grade == 2:
        M2.append(2)
    elif gen ==0 and grade == 3:
        M3.append(3)
    elif gen ==0 and grade == 4:
        M4.append(4)
    elif gen ==0 and grade == 5:
        M5.append(5)
    elif gen ==0 and grade == 6:
        M6.append(6)
    elif gen ==1 and grade == 1:
        W1.append(1)
    elif gen ==1 and grade == 2:
        W3.append(2)
    elif gen ==1 and grade == 3:
        W4.append(3)
    elif gen ==1 and grade == 4:
        W5.append(4)
    elif gen ==1 and grade == 5:
        W5.append(5)
    elif gen ==1 and grade == 6:
        W6.append(6)

cnt=0
for i in range(len(school)):
    x = len(school[i])
    if x !=0 and x<=K:
        cnt+=1
    elif x >K:
        if x%K ==0:
            cnt+=x//K
        else:
            cnt+=x//K+1
print(cnt)


