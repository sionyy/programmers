N=int(input())
lst=set()
for i in range(N):
    lst.add(input())

new=sorted(lst,key=lambda x:(len(x),x))
for i in range(len(new)):
    print(new[i])