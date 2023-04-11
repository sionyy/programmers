n=int(input())
start=n//5
now3=1

def check():
    if n%5==0:
        return n//5

    while True:
        global start,now3
        if start*5+now3*3==n:
            return start+now3
        elif start*5+now3*3<n:
            now3+=1
        elif start*5+now3*3>n:
            start-=1
        if start==-1:
            return -1

print(check())