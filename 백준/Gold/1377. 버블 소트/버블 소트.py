import sys
input = sys.stdin.readline

N=int(input())
lst=[]
lst2=[]
for i in range(N):
    lst.append((int(input()),i))

lst2=lst[:]
lst2.sort()

ans=[]
for i in range(N):
    ans.append(lst2[i][1]-lst[i][1])
print(max(ans)+1)