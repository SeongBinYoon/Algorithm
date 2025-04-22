# 1037 약수

import sys
input = sys.stdin.readline

# N의 진짜 약수의 개수
n = int(input())
# N의 진짜 약수
lst = list(map(int, input().split(' ')))

new_lst = sorted(lst)
print(new_lst[0]*new_lst[-1])