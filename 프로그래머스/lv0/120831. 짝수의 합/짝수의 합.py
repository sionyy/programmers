def solution(n):
    sum1 = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum1 = sum1 + i
    return sum1