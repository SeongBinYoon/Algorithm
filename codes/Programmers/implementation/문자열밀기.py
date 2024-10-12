# 문자열 밀기

def solution(A, B):
    answer = 0
    acc = 0
    if A == B:
        return 0
    for _ in range(len(A)):
        # 오른쪽으로 밀기
        A = A[-1] + A[:-1]
        acc += 1
        if A == B:
            answer = acc
            acc = 0
            break
    if answer == 0:
        answer = -1
    return answer