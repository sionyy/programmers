from collections import deque
import sys
input=sys.stdin.readline

n=int(input())

lst=[]
for i in range(n):
    lst.append(int(input()))

q=deque(sorted(lst))

for i in range(n):
    print(q.popleft())