def solution(slice, n):
    lst_slice = []
    count =0
    for i in range(1,100):
        lst_slice.append(i*slice)

    for j in lst_slice:
        count = count+1
        answer = count
        if j >= n: #14 10
            break
    return answer