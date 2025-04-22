# 18258 큐2

import sys
input = sys.stdin.readline
from collections import deque

dq = deque([])
n = int(input())
for _ in range(n):
    c = list(input().strip().split(' '))
    if c[0] == 'push':
        dq.append(int(c[1]))
    elif c[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif c[0] == 'size':
        print(len(dq))
    elif c[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif c[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])