n=int(input())
result=[]
ans=0
for i in range(10000):
    if n < i*i:
        ans=i-1
        break
for i in range(1,ans+1):
    if n >=i*i:
        result.append((n//i)-i+1)
print(sum(result))