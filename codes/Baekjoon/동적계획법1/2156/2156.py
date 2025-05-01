# 2156 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
# 포도주 잔 리스트, 누적값 리스트
wine, table = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
for i in range(1, n+1):
    wine[i] = int(input())

# DP
# 포도주 잔이 1개, 2개인 경우, 다 마시는 것이 최댓값
if n == 1 or n == 2:
    print(sum(wine))
# 포도주 잔이 3개 이상인 경우, i번째 포도주를 마시는 데에 두 가지로 나뉨 + i번째 안마시는 경우
# 1. i-2번째를 마시고 i번째를 마심
# 2. i-3번째를 마시고 i-1번째를 마시고 i번째를 마심
# 3. i번째 안마심
else:
    table[1] = wine[1]
    table[2] = table[1] + wine[2]
    for j in range(3, n+1):
        table[j] = max(table[j-2] + wine[j], table[j-3] + wine[j-1] + wine[j], table[j-1])
    print(table[n])