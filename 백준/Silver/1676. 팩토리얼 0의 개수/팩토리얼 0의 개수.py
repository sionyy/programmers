T=int(input())
n=1
for i in range(1,T+1):
    n*=i
n=list(str(n))
start=len(n)-1

cnt=0
while True:
    if n[start]!='0':
        break
    elif n[start]=='0':
        cnt+=1
        start-=1
print(cnt)