# 2178 미로 탐색

import sys
input = sys.stdin.readline
from collections import deque

# 그래프
g = []

# 입력 - 그래프 생성
# 행, 열
n, m = map(int, input().split())
for _ in range(n):
    g.append(list(map(int, input().strip())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(g, a, b):
    # 큐 생성 및 시작점 추가
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계선에 닿은 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우
            if g[nx][ny] == 0:
                continue
            # 올바른 길 & 방문하지 않은 길인 경우
            if g[nx][ny] == 1:
                # 큐에 삽입
                queue.append((nx, ny))
                # 카운팅
                g[nx][ny] = g[x][y] + 1
    return g[n-1][m-1]

# 출력
print(bfs(g, 0, 0))