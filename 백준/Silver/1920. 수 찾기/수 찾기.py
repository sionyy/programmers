import sys
input=sys.stdin.readline
from collections import deque
N=int(input())
lst=list(map(int,input().split()))
M=int(input())
check=list(map(int,input().split()))
lst.sort()

for i in range(M):
    if check[i] in lst:
        print(1)
        continue
    else:
        print(0)
