n=int(input())

lst=[]
cnt=0
for i in range(10000000):
    if '666' in str(i):
        lst.append(i)
        cnt+=1
        if cnt==n:
            break
print(lst[-1])
