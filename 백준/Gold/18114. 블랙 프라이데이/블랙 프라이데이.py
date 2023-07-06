import sys
input=sys.stdin.readline
N,target=map(int,input().split())
data=list(map(int,input().split()))
data.sort()

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

def find():
    #1개 찾기
    if binary_search(data,0,N-1,target):
        return 1

    left,right=0,N-1
    while left<right:
        summ=data[left]+data[right]
        if summ==target: #2개 검사
            return 1
        elif summ>target:
            right-=1
        else:
            new_target = target-summ
            if data[left]!=new_target and data[right]!=new_target and binary_search(data,left,right,new_target):
               return 1
            left+=1
    return 0

print(find())