st=input()
if len(st)<4 or len(st)%4!=0 or st[0]!='w':
    print(0)
    exit()

now=0
stack=0
ans=1

def check():
    global now,stack,ans
    while now<=len(st):
        if st[now]=='w':
            if now+3>len(st):
                ans=0
                return
            stack+=1
            now+=1
            if now > len(st):
                return
        elif st[now]=='o' and stack==1:
            if st[now:now+3]=='olf':
                now+=3
                stack=0
                if now >= len(st):
                    return
            else:
                ans=0
                return

        elif st[now]=='o' and stack>1:
            if st[now:now+stack]=='o'*stack and st[now+stack:now+stack*2]=='l'*stack and st[now+stack*2:now+stack*3]=='f'*stack:
                now+=stack*3
                stack=0
                if now>=len(st):
                    return
            else:
                ans=0
                return
        else:
            ans=0
            return


check()
print(ans)