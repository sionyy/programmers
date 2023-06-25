#N개의 강의 개수
#M개의 블루레이 개수 (같은 크기)
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
lst=list(map(int,input().split()))
left=max(lst)
right=sum(lst)

while left<=right:
    mid = (left + right) // 2
    bluelay = 1
    summ = 0

    for i in range(N):
        if summ+lst[i]>mid:
            summ = lst[i]
            bluelay+=1
        else:
            summ+=lst[i]
    if bluelay>M:
        left=mid+1
    else:
        right=mid-1
print(left)