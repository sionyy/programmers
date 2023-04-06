"""
A : 5분
B : 1분
C : 10초
"""

A=300
B=60
C=10

n=int(input())
def greedy(n):
    if n%10 !=0:
        return print(-1)
    cntA=0
    cntB=0
    cntC=0
    while True:
        if n-A>=0:
            n-=A
            cntA+=1
        elif n-B>=0:
            n-=B
            cntB+=1
        elif n-C>=0:
            n-=C
            cntC+=1
        if n==0:
            return print(*(cntA,cntB,cntC))

greedy(n)