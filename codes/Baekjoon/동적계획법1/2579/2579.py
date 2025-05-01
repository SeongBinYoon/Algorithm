# 2579 계단 오르기

import sys
input = sys.stdin.readline

# 입력
n = int(input())
# 계단 입력 리스트, 누적값 리스트
stair, table = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
for i in range(1, n+1):
    stair[i] = int(input())

# DP
# 계단이 1개, 2개일 때는 다 밟는 것이 최댓값
if n == 1 or n == 2:
    print(sum(stair))
# 계단이 3개 이상인 경우, i번 째 계단을 오르는데에 두 가지로 나뉨
# 1. i-3을 밟고 i-1을 밟음
# 2. i-2를 밟음
else:
    table[1] = stair[1]
    table[2] = table[1] + stair[2]
    for j in range(3, n+1):
        table[j] = max(table[j-3] + stair[j-1], table[j-2]) + stair[j]
    print(table[n])