# 11659 구간 합 구하기4

import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))

# 누적 합 알고리즘
for i in range(1, n):
    lst[i] = lst[i-1] + lst[i]
# 입력
for _ in range(m):
    i, j = map(int, input().split(' '))
    if i == 1:
        print(lst[j-1])
    else:
        print(lst[j-1] - lst[i-2])