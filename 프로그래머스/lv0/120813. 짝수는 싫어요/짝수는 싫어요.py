def solution(n):
    if n%2 ==1:
        n = n+1
    result = []
    for i in range(n):
        if i%2 ==1:
            result.append(i)

    return result