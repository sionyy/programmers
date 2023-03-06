T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    # W B R 순서
    arr=list(input() for _ in range(N))
    
    notW=[]
    notB=[]
    notR=[]
    for i in range(N):
        w = 0
        b = 0
        r = 0
        for j in range(M):
            if arr[i][j] != 'W':
               w+=1
            if arr[i][j] != 'B':
               b+=1
            if arr[i][j] != 'R':
               r+=1
        notW.append(w)
        notB.append(b)
        notR.append(r)
    result=[]
    sumW=0
    for i in range(0,N-2): # 1~2
        sumB=0
        sumW+=notW[i]
        for j in range(i+1,N-1):
            sumB+=notB[j]
            sumR=0
            for k in range(j+1,N):
                sumR+=notR[k]
            result.append(sumW+sumB+sumR)
    print(f'#{tc} {min(result)}')
