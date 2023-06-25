n=int(input())
def 소수판별(숫자):
    for i in range(2,(int(숫자**0.5))+1):
        if int(숫자)%i==0:
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if 소수판별(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
