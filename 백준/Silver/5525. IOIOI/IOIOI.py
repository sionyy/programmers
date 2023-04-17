import sys
input=sys.stdin.readline

N=int(input())
s=int(input())
st=input()

first = 'I'+'OI'*N

cnt=0
for i in range(len(st)-len(first)):
    if first ==st[i:i+len(first)]:
        cnt+=1
print(cnt)