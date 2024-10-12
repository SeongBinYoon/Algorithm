# 잘라서 배열로 저장하기

def solution(my_str, n):
    answer = []
    s = ''
    while my_str != '':
        s = my_str[:n]
        my_str = my_str[n:]
        answer.append(s)
        s = ''
    return answer