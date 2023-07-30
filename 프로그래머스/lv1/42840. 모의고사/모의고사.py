#12345
#21232425
#3311224455
def solution(answers):
    answer = []
    supo1=[1,2,3,4,5]*2000
    supo2=[2,1,2,3,2,4,2,5]*1250
    supo3=[3,3,1,1,2,2,4,4,5,5]*1000
    ans=[0,0,0]
    for i in range(len(answers)):
        if supo1[i]==answers[i]:
            ans[0]+=1
        if supo2[i]==answers[i]:
            ans[1]+=1
        if supo3[i]==answers[i]:
            ans[2]+=1
    
    result=max(ans)
    for j in range(3):
        if result==ans[j]:
            answer.append(j+1)
    
    return answer