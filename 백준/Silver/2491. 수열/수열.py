N=int(input())
lst=list(map(int,input().split()))

time=0
pl=1
mi=1
box=[]
while True:
    if len(lst)==1:
        box.append(1)
        break
    if lst[time] <= lst[time+1]:
        pl+=1
    elif lst[time]>lst[time+1]:
        box.append(pl)
        pl=1

    if lst[time] >= lst[time+1]:
        mi+=1
    elif lst[time]<lst[time+1]:
        box.append(mi)
        mi=1

    time+=1
    if time==N-1:
        box.append(pl)
        box.append(mi)
        break
print(max(box))