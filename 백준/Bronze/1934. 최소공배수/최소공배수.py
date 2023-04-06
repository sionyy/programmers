import sys
input = sys.stdin.readline
n = int(input())
def soin(num):
    lst = []
    while num != 1:
        for i in range(2, num + 1):
            if num % i == 0:
                num = num // i
                lst.append(i)
                break
            else:
                pass
    return lst

for repeat in range(n):
    a, b = map(int, input().split())
    lstA = soin(a)
    lstB = soin(b)

    full_lst=lstA+lstB

    ans=[]
    for i in range(len(full_lst)):
        if full_lst[i] not in ans:
            MAXX=max(lstA.count(full_lst[i]),lstB.count(full_lst[i]))
            for k in range(MAXX):
                ans.append(full_lst[i])
    result=1
    for i in range(len(ans)):
        result*=ans[i]
    print(result)
