TT=list(input())
end=len(TT)
start=0
cnt=10


while start!=end-1:
    if TT[start] == TT[start+1]:
        cnt+=5
    else:
        cnt+=10
    start+=1
print(cnt)