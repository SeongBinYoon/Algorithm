# 문자열 계산하기

def solution(my_string):
    answer = 0
    res = 0
    lst = my_string.split(' ')
    while len(lst) != 1:
        if lst[1] == '+':
            res = int(lst[0]) + int(lst[2])
        else:
            res = int(lst[0]) - int(lst[2])
        lst = [str(res)] + lst[3:]
    answer = res
    return answer