import sys
input = sys.stdin.readline
N=int(input())
bucket=[0]*10001
for i in range(N):
    bucket[int(input())]+=1

for i in range(10001):
    if bucket[i] !=0:
        for _ in range(bucket[i]):
            print(i)