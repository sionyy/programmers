def solution(my_string):
    sum =''
    lst_my_string = list(my_string)
    lst_my_string.reverse()
    for i in lst_my_string:
        sum = sum+i
    return sum