N=int(input())
s=int(input())
st=list(input())

first = ['I']+['O','I']*N

cnt=0
for i in range(len(st)-len(first)+1):
    if first ==st[i:i+len(first)]:
        cnt+=1
print(cnt)