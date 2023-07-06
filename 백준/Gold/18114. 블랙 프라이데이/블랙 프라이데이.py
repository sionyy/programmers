import sys
input = sys.stdin.readline

def solution(now):
    N, target = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    box = set([0] + lst) # 중요
    if target in box: #한개
        return 1
    while now < N-1: #끝까지 탐색
        left, right = lst[now], lst[N-1] #left, right 설정
        new_target = target-left-right
        #set(0)을 추가하여 2개와 3개를 동시에 검색
        if new_target != left and new_target != right and new_target in box:
            return 1
        if new_target < 0:
            N-=1
        else:
            now+=1
    return 0



print(solution(0))