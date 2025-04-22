# 11047 동전 0

import sys
input = sys.stdin.readline

lst = []
cnt = 0

# 입력
n, k = map(int, input().split())
for _ in range(n):
    lst.append(int(input()))

# 역순 정렬
lst = sorted(lst, reverse=True)

# 동전 훑기
for i in lst:
    # k보다 작거나 같은 동전들로 사용
    if i <= k:
        cnt += k // i
        k = k % i
print(cnt)