n=int(input())
for i in range(n):
    st=input()
    cnt=0
    start=0
    now=0
    while True:
        if start==len(st):
            break
        if st[start]=='O':
            now+=1
            cnt+=now
        else:
            now=0
        start+=1
    print(cnt)