# 세균 증식

def solution(n, t):
    answer = 0
    for i in range(t):
        n *= 2
    answer = n
    return answer