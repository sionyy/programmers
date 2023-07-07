import sys
input = sys.stdin.readline
N=int(input())
numbers=list(map(int,input().split()))
order=list(map(int,input().split()))

minn = 10**9
maxx = -10**9

def calculator(plus,minus,mul,div,value,level):
    global minn,maxx
    if level == N:
        minn=min(minn,value)
        maxx=max(maxx,value)
        return

    if plus>0:
        calculator(plus-1,minus,mul,div,value+numbers[level],level+1)
    if minus>0:
        calculator(plus,minus-1,mul,div,value-numbers[level],level+1)
    if mul > 0:
        calculator(plus, minus,mul-1,div, value*numbers[level], level + 1)
    if div> 0:
        if value>0:
            calculator(plus, minus,mul,div-1, value//numbers[level], level + 1)
        else:
            calculator(plus, minus,mul,div-1, -(value // -numbers[level]), level + 1)

calculator(order[0],order[1],order[2],order[3],numbers[0],1)

print(maxx)
print(minn)
