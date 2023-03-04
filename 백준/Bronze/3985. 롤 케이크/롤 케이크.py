# L 롤케이크 길이
# N 방청객의 수
# P,K 원하는 조각 범위

#출력
# 1) 범위가 가장 큰 행
# 2) 리스트에 번호가 가장 많이 적힌 숫자

"""
1. 10짜리 리스트 만들기
2. 3번 반복하기
3. 범위에 맞게 숫자 채우기
"""

N=int(input())
H=int(input())
lst = [0]*N

MAX=0
MAXk=0
for k in range(H):
    st,end = map(int,input().split())
    for i in range(len(lst)):
        for j in range(st-1,end):
            if lst[j] == 0:
                lst[j] = k+1
    if end-st > MAX:
        MAX = end-st
        MAXk = k+1
print(MAXk)



bucket=[0]*N
for i in range(N):
    bucket[lst[i]]+=1
# print(bucket)

lst_max=0
maxi=0
for i in range(len(bucket)):
    if i>0:
        if bucket[i]>lst_max:
            lst_max = bucket[i]
            maxi = i

print(maxi)