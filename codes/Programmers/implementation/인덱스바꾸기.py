# 인덱스 바꾸기

def solution(my_string, num1, num2):
    answer = ''
    lst = []
    for s in my_string:
        lst.append(s)
    tmp = lst[num2]
    lst[num2] = lst[num1]
    lst[num1] = tmp
    
    for word in lst:
        answer += word
    return answer