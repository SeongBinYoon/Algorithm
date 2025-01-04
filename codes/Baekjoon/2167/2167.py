# 2167 2차원 배열의 합

import sys
input = sys.stdin.readline

lst = []
n, m = map(int, input().split(' '))
for _ in range(n):
    box = list(map(int, input().split(' ')))
    lst.append(box)
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split(' '))
    i, j, x, y = i-1, j-1, x-1, y-1
    acc = 0
    for s in range(i, x+1):
        for t in range(j, y+1):
            acc += lst[s][t]
    print(acc)