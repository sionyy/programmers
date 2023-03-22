T= int(input())
for tc in range(T):
    N=int(input())
    lst=[]
    for i in range(N):
        lst.append(input().split())

    MAXX=0
    ans=''
    for i in range(N):
        if MAXX<int(lst[i][0]):
            MAXX = int(lst[i][0])
            ans = lst[i][1]
    print(ans)