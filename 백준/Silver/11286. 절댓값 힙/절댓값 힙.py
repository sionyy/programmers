from heapq import heappush,heappop
import sys
input=sys.stdin.readline
N=int(input())
lst=[]

for i in range(N):
    a=int(input())
    if a !=0:
        heappush(lst, [abs(a),a])
    elif a==0:
        if len(lst)==0:
            print(0)
        else:
            print(heappop(lst)[1])