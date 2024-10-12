# 숫자찾기

def solution(num, k):
    answer = 0
    if str(k) in str(num):
        answer = str(num).find(str(k)) + 1
    else:
        answer = -1
    return answer