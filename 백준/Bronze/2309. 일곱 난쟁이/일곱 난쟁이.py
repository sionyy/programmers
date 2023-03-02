lst=[]
for i in range(9):
    lst.append(int(input()))
lst.sort()

N=len(lst)
All=sum(lst) # 140
ans = All-100

flag=0
for i in range(N-1):
    if flag:
        break
    for j in range(i+1,N):
        if flag:
            break
        if lst[i]+lst[j]==ans:
            del lst[j]
            del lst[i]
            flag=1

for i in lst:
    print(i)