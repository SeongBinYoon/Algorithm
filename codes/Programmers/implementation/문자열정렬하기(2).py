# 문자열 정렬하기(2)

def solution(my_string):
    answer = ''
    my_string = sorted(my_string.lower())
    for s in my_string:
        answer += s
    return answer