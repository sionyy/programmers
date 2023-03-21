import sys
input = sys.stdin.readline
N=int(input())
bucket=[0]*10001
for i in range(N):
    bucket[int(input())]+=1

lst=[]
for i in range(len(bucket)):
    if bucket[i] !=0:
        lst.append((bucket[i],i))

for i in range(len(lst)):
    for j in range(lst[i][0]):
        print(lst[i][1])