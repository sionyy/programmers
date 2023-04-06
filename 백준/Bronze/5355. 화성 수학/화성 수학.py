"""
@ *3
% +5
# -7
{num:.2f}
"""

n=int(input())
for i in range(n):
    lst=list(map(str,input().split()))
    start=float(lst[0])
    for j in range(len(lst)):
        if lst[j]=='@':
            start=start*3
        elif lst[j]=='%':
            start+=5
        elif lst[j]=='#':
            start-=7
    print(f'{start:.2f}')

