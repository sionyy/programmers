import sys
input = sys.stdin.readline

N = int(input())                            #재료 개수
complete = int(input())                     #갑옷 되는 번호
lst_item = list(map(int, input().split()))


MAX = 0
for i in range(len(lst_item)): # bucket 생성을 위한 MAX값 할당
    if lst_item[i]>MAX:
        MAX = lst_item[i]

bucket = [0]*(MAX+1)           # bucket 생성
for i in range(len(lst_item)):
    bucket[lst_item[i]]+=1

sortitem=[]
for i in range(len(bucket)):
    for j in range(bucket[i]):
        sortitem.append(i) #정렬된 리스트 == sortitem



count = 0   #투포인터를 위한 변수 할당
start = 0
end = N-1


while start < end:
    if sortitem[start] + sortitem[end] < complete:
        start += 1
    elif sortitem[start] + sortitem[end] > complete:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)