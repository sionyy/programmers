#학생수 n [2~30]
#도난 lost
#여벌 reserve

def solution(n, lost, reserve):
    answer = 0
    lst=[1]*(n+2)
    lst2=[1]*(n+2)
    for i in lost:
        lst[i]=0
        lst2[i]=0
    
    for s in lost:
        if s in reserve:
            reserve.remove(s)
            lst[s]=1
            lst2[s]=1
    print(reserve)
    print(lst)

    for j in reserve:
        if lst[j-1]==0:
            lst[j-1]=1

        elif lst[j+1]==0:
            lst[j+1]=1
                
    for k in reserve:
        if lst2[k+1]==0:
            lst2[k+1]=1                
        elif lst2[k-1]==0:
            lst2[k-1]=1

                
    ans1=0
    ans2=0
    for k in range(1,len(lst)-1):
        if lst[k] ==1:
            ans1+=1
        if lst2[k]==1:
            ans2+=1
    answer=max(ans1,ans2)
    print(lst)
    print(lst2)
    return answer