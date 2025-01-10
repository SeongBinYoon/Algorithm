# 11441 합 구하기

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split(' ')))
m = int(input())

# 누적 합 알고리즘
for i in range(1, n):
    lst[i] = lst[i-1] + lst[i]

for _ in range(m):
    i, j = map(int, input().split(' '))
    if i == 1:
        print(lst[j-1])
    else:
        print(lst[j-1] - lst[i-2])