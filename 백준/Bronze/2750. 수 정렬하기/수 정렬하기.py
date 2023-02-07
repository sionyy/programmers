x = int(input())
lst = []
for i in range(x):
    lst.append(int(input()))

lst= sorted(lst)
for i in range(len(lst)):
    print(lst[i])