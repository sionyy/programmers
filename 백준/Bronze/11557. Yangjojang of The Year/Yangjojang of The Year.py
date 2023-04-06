T=int(input())
for tc in range(T):
    n=int(input())
    MAXX=0
    MAXuniv=''
    for i in range(n):
        temp = list(map(str,input().split()))
        if int(temp[1])>MAXX:
            MAXX=int(temp[1])
            MAXuniv=temp[0]
    print(MAXuniv)