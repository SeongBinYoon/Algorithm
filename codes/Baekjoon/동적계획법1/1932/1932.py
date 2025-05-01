# 1932 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())
# 누적값 리스트
table = [0] * n

# 입력
for i in range(n):
    table[i] = list(map(int, input().split()))

# DP
# 각 줄 훑기
for j in range(1, n):
    # 한 줄의 각 자리 훑기
    for k in range(j+1):
        # 좌대각, 우대각 두가지 고려, 각 줄의 첫번째와 마지막은 좌대각, 우대각이 없음을 고려
        # 각 줄의 첫번째 값인 경우, 이전 줄 우대각 그대로 누적
        if k == 0:
            table[j][k] = table[j-1][k] + table[j][k]
        # 각 줄의 마지막 값인 경우, 이전 줄 좌대각 그대로 누적
        elif k == j:
            table[j][k] = table[j-1][k-1] + table[j][k]
        # 각 줄의 첫번째, 마지막 값이 아닌 경우, 이전 줄 좌대각과 우대각 중 최댓값 누적
        else:
            table[j][k] = max(table[j-1][k-1], table[j-1][k]) + table[j][k]
# 마지막 줄 최대누적값 출력
print(max(table[n-1]))