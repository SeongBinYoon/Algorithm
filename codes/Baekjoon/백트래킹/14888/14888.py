# 14888 연산자 끼워넣기

import sys
input = sys.stdin.readline

# 주어진 초기 최댓값, 최솟값(비교를 위해 최솟값이 초기 maxval)
maxval = -1000000000
minval = 1000000000

# Backtracking + DFS
def dfs(add, sub, mul, div, acc, idx):
    
    global maxval, minval
   
    # 노드 종료 조건
    # 인덱스가 주어진 수열 개수와 같으면 종료
    if idx == n:
        maxval = max(acc, maxval)
        minval = min(acc, minval)
        return
    
    # 각 연산: 0(False)이 아닐 경우 재귀 호출(연산자 개수 -1, 누적 연산, lst의 다음 인덱스로)
    if add:
        dfs(add - 1, sub, mul, div, acc + lst[idx], idx + 1)
    if sub:
        dfs(add, sub - 1, mul, div, acc - lst[idx], idx + 1)
    if mul:
        dfs(add, sub, mul - 1, div, acc * lst[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(acc / lst[idx]), idx + 1)

n = int(input())
lst = list(map(int, input().split()))
op = list(map(int, input().split()))

# 파라미터 순서대로 +, -, *, /, 누적 값, 주어진 수열(리스트)의 인덱스-cnt 역할
dfs(op[0], op[1], op[2], op[3], lst[0], 1)
print(maxval)
print(minval)