# 4963 섬의 개수

import sys
input = sys.stdin.readline
from collections import deque

# 이동(행, 열) - 좌우상하, 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# bfs
def bfs(g, a, b):
    queue = deque()
    queue.append((a, b))
    # 시작점 2로 시작
    g[a][b] = 2
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if g[nx][ny] == 1:
                queue.append((nx, ny))
                g[nx][ny] = g[x][y] + 1
    # 섬의 크기 리턴
    return g[x][y] - 1

# 입력
while True:
    # 그래프 초기화화
    g, res = [], []
    w, h = map(int, input().split())
    if w == h == 0:
        break
    # 그래프
    for _ in range(h):
        g.append(list(map(int, input().split())))
    # 함수 호출
    for i in range(h):
        for j in range(w):
            # 안 센 곳은 세기
            if g[i][j] == 1:
                res.append(bfs(g, i, j))
    # 개수 출력
    print(len(res))