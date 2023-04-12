import sys
input=sys.stdin.readline
N=int(input())
lst=[]
for i in range(N):
    a,b=map(int,input().split())
    lst.append((a,b))

new=sorted(lst,key=lambda x:(x[1],x[0]))
for i in range(N):
    print(*new[i])