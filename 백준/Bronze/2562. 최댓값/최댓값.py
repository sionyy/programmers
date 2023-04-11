MAXX=0
maxi=0
for i in range(9):
    a=int(input())
    if MAXX<a:
        MAXX=a
        maxi=i+1
print(MAXX)
print(maxi)