# 17219 비밀번호 찾기

import sys
input = sys.stdin.readline

dic = {}
n, m = map(int, input().split(' '))
for _ in range(n):
    key, value = input().split(' ')
    dic[key] = value
for _ in range(m):
    print(dic[input()])