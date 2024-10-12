# 가장 큰 수 찾기

def solution(array):
    answer = []
    a = max(array)
    b = array.index(a)
    answer = [a, b]
    return answer