# 1912 연속합

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# DP: memoization
for i in range(1, n):
    lst[i] = max(lst[i], lst[i]+lst[i-1])
print(max(lst))