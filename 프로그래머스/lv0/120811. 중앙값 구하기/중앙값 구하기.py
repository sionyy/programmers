def solution(array):
    length = len(array)

    result = int(len(array)/2)

    answer = sorted(array)[result]
    return answer
