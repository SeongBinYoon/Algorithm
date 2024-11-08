# k의 개수

def solution(i, j, k):
    answer = 0
    # 일렬로 나열할 문자열
    itoj = ''
    # i~j까지 문자열 나열
    for num in range(i, j+1, 1):
        itoj += str(num)
    # 문자열에서 k 탐색
    answer = itoj.count(str(k))
    return answer