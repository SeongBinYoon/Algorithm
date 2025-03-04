# 9184 신나는 함수 실행

import sys
input = sys.stdin.readline

# table 정의, 3차원 리스트
table = [[[None] * 100 for _ in range(100)] for _ in range(100)]

# DP
def solution(a, b, c):
    # 기저: 하나라도 0 이하라면 1
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # 해당 리스트의 값이 저장되어 있지 않다면
    if table[a][b][c] is None:
        # a, b, c 모두 20보다 크다면
        if a > 20 or b > 20 or c > 20:
            table[a][b][c] = solution(20, 20, 20)
        # a < b < c라면
        elif a < b and b < c:
            table[a][b][c] = solution(a, b, c-1) + solution(a, b-1, c-1) - solution(a, b-1, c)
        # 그 외
        else:
            table[a][b][c] = solution(a-1, b, c) + solution(a-1, b-1, c) + solution(a-1, b, c-1) - solution(a-1, b-1, c-1)
    # 해당 리스트의 값이 저장되어 있다면 값 return
    return table[a][b][c]
    
# 입력/함수 호출/출력
while True:
    a, b, c = map(int, input().split())
    # -1, -1, -1이면 프로그램 종료
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) =", solution(a, b, c))


'''
# 기존 함수
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
print(w(50, 50, 50))
'''