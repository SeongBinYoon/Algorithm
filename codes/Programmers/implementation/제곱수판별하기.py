# 제곱수 판별하기

def solution(n):
    answer = 2
    for i in range(n):
        if i**2 == n:
            answer = 1
            break
    return answer