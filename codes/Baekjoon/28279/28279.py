# 28279 덱 2

from collections import deque

lst = []
dq = deque([])
n = int(input())
for _ in range(n):
    c = list(map(int, input().split(' ')))
    lst.append(c)

for i in range(len(lst)):
    if lst[i][0] == 1:
        dq.appendleft(lst[i][1])
    elif lst[i][0] == 2:
        dq.append(lst[i][1])
    elif lst[i][0] == 3:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif lst[i][0] == 4:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
            dq.pop()
    elif lst[i][0] == 5:
        print(len(dq))
    elif lst[i][0] == 6:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif lst[i][0] == 7:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif lst[i][0] == 8:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])