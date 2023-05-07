from heapq import heappush, heappop, heapify
import sys
input=sys.stdin.readline
N=int(input())
heap=[]

for i in range(N):
  a=int(input())
  if a == 0 and len(heap)==0:
    print(0)
  elif a==0:
    print(heappop(heap)[1])
  else:
    heappush(heap,(-a,a))
