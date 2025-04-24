# 1149 RGB거리

import sys
input = sys.stdin.readline

n = int(input())
# 입력 및 누적값을 담을 리스트 초기화
table = [0] * n

# 입력
for i in range(n):
    table[i] = list(map(int, input().split()))

# DP
for i in range(1, n):
    # i번째 집이 R일 때, 이전 집의 G, B 중 최솟값 + 이 집의 R값
    table[i][0] = min(table[i-1][1], table[i-1][2]) + table[i][0]
    # i번째 집이 G일 때, 이전 집의 R, B 중 최솟값 + 이 집의 G값
    table[i][1] = min(table[i-1][0], table[i-1][2]) + table[i][1]
    # i번째 집이 B일 때, 이전 집의 R, G 중 최솟값 + 이 집의 B값
    table[i][2] = min(table[i-1][0], table[i-1][1]) + table[i][2]

# 마지막 누적값(마지막 집 R/G/B일 때 누적값) 중 최솟값
print(min(table[n-1]))