# 2485 가로수

import sys
input = sys.stdin.readline

# 유클리드 호제법
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

# 각 나무 간 차이 저장
diff = []
n = int(input())
tmp = 0
for _ in range(n):
    pos = int(input())
    if tmp != 0:
        diff.append(pos - tmp)
    tmp = pos

# 최대공약수 구하기
val = diff[0]
for i in range(1, len(diff)):
    val = gcd(val, diff[i])

# 각 나무 사이 심을 나무의 수
tree = 0
for j in range(len(diff)):
    tree += diff[j] // val - 1
print(tree)