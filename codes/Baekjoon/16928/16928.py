# 16928 뱀과 사다리 게임

import sys
input = sys.stdin.readline
from collections import deque

# 사다리, 뱀 정보 딕셔너리
ladder = {}
snake = {}

# 입력(사다리 수, 뱀 수)
n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

# 그래프 생성
board = [0 for _ in range(101)]

# 이동(주사위)
d = [1, 2, 3, 4, 5, 6]

# bfs
def bfs(start):
    queue = deque()
    queue.append(start)
    board[start] = 1
    while queue:
        # 꺼냄
        v = queue.popleft()
        # 이동
        for i in range(6):
            n = v + d[i]
            # 100칸을 넘어가는 경우
            if n > 100:
                continue
            # 이동한 곳에 사다리가 있다면 n을 해당 값으로 이동
            if n in ladder:
                n = ladder[n]
            # 이동한 곳에 뱀이 있다면 n을 해당 값으로 이동
            elif n in snake:
                n = snake[n]
            # 이동한 곳을 확인
            if board[n] == 0:
                queue.append(n)
                board[n] = board[v] + 1

bfs(1)
print(board[-1]-1)