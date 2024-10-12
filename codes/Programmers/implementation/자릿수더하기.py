# 자릿수 더하기

def solution(n):
    answer = 0
    while n != 0:
        target = 10 ** (len(str(n))-1)
        answer += (n // target)
        n %= target
    return answer