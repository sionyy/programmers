# import sys
# sys.stdin = open('TT.txt')
T=int(input())
for tc in range(1,T+1):
    st = list(map(int,input()))
    flag = [-1 for _ in range(len(st))]
    tempst=[]
    for i in range(len(st)):
        tempst.append(st[i])

    SUM=0
    for i in range(len(st)):
        if SUM>=i:
            flag[i] = 0
        elif SUM<i:
            flag[i] = i-SUM
            st[i]+=i-SUM
        SUM+=st[i]
    ans=sum(flag)
    print(f'#{tc} {ans}')