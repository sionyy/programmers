n=int(input())
Q1=0
Q2=0
Q3=0
Q4=0
AXIS=0
for i in range(n):
    a,b=map(int,input().split())
    if a==0 or b == 0:
        AXIS+=1
    elif a>0 and b>0:
        Q1+=1
    elif a>0 and b<0:
        Q4+=1
    elif a<0 and b<0:
        Q3+=1
    elif a<0 and b>0:
        Q2+=1
lst=['Q1','Q2','Q3','Q4','AXIS']
value=[Q1,Q2,Q3,Q4,AXIS]
for i in range(5):
    print(f'{lst[i]}: {value[i]}')