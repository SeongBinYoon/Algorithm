# 2583 영역 구하기

import sys
input = sys.stdin.readline
from collections import deque

# 입력
m, n, k = map(int, input().split())
# 그래프(0=갈 수 있는 곳, 1=막힌 곳)
g = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # 그래프 색칠
    for i in range(m - y2, m - y1):
        for j in range(x1, x2):
            g[i][j] = 1

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(g, a, b):
    queue = deque()
    queue.append((a, b))
    g[a][b] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if g[nx][ny] == 0:
                queue.append((nx, ny))
                g[nx][ny] = 1
                cnt += 1
                # g[nx][ny] = g[x][y] + 1 -> 최단 거리 구하는 것, 개수 세는데 적합x
    return cnt

res = []
for i in range(m):
    for j in range(n):
        if g[i][j] == 0:
            res.append(bfs(g, i, j))

print(len(res))
res.sort()
for s in res:
    print(s, end=' ')