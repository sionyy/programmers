n=int(input())
for i in range(n):
    r,e,c=map(int,input().split())
    if e-c > r:
        ans="advertise"
    elif e-c==r:
        ans="does not matter"
    else:
        ans="do not advertise"
    print(ans)
