import sys
input = sys.stdin.readline

def solution(now):
    global N,target,lst
    box = set([0] + lst)
    if target in box:
        return 1
    while now < N-1:
        left, right = lst[now], lst[N-1]
        new_target = target - left - right
        if new_target != left and new_target != right and new_target in box:
            return 1
        if new_target < 0:
            N -= 1
        else:
            now += 1
    return 0

N, target = map(int, input().split())
lst = sorted(list(map(int, input().split())))
print(solution(0))