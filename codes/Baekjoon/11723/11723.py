# 11723 집합

import sys
input = sys.stdin.readline

# 리스트(스택)로 접근 -> 시간초과
# 집합(set)으로 접근
s = set()
n = int(input())
for _ in range(n):
    lst = list(input().split(' '))

    if lst[0] == 'add':
        if int(lst[1]) not in s:
            s.add(int(lst[1]))

    elif lst[0] == 'remove':
        if int(lst[1]) in s:
            s.remove(int(lst[1]))

    elif lst[0] == 'check':
        if int(lst[1]) in s:
            print(1)
        else:
            print(0)

    elif lst[0] == 'toggle':
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
        else:
            s.add(int(lst[1]))

    elif lst[0] == 'all\n':
        s.clear()
        s = set(i for i in range(1, 21))

    elif lst[0] == 'empty\n':
        s.clear()