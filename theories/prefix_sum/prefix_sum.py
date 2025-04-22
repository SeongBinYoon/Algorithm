# 누적 합(Prefix sum) 알고리즘
# BOJ #11659

# Test code
#5 3
#5 4 3 2 1
#1 3
#2 4
#5 5

import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))

# 누적 합 알고리즘
# 기존 리스트: 5,4,3,2,1
# 누적 합 적용 리스트: 5,9,12,14,15
# 1 3 => 12
# 2 4 => 9
# 5 5 => 1
for i in range(1, n):
    lst[i] = lst[i-1] + lst[i]

# 입력
for _ in range(m):
    i, j = map(int, input().split(' '))
    if i == 1:
        print(lst[j-1])
    else:
        print(lst[j-1] - lst[i-2])