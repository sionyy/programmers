N = int(input())

lst= list(map(int, input().split()))

MAX=max(lst)
#문제 : 점수 / MAX * 100

gop = (1/MAX)*100
print(sum(lst)*gop/N)

