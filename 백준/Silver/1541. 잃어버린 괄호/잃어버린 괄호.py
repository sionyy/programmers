full = input().split('-')
first=full[0]
second=full[1:]
summ=0

for i in first.split('+'):
    summ+=int(i)

for i in second:
    for j in i.split('+'):
        summ-=int(j)
print(summ)