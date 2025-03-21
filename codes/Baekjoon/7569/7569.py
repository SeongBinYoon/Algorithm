# 7569 토마토

import sys
input = sys.stdin.readline
from collections import deque

box = []
# 열, 행, 높이
m, n, h = map(int, input().split())
for _ in range(h):
    floor = []
    for _ in range(n):
        floor.append(list(map(int, input().split())))
    box.append(floor)

# 좌우 앞뒤 상하
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 큐 선언
queue = deque()

# bfs
def bfs():
    # 큐가 빌 때까지 반복
    while queue:
        # 꺼냄(x행, y열)
        z, x, y = queue.popleft()
        # 상하좌우앞뒤 확인
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 경계선 밖이면 다시
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                continue
            # -1이면(들어있지 않은 칸) 다시
            if box[nz][nx][ny] == -1:
                continue
            # 0이면(익지 않은 곳)
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append((nz, nx, ny))

# 높이, 행과 열을 돌며 1인 곳을 시작점으로 큐에 삽입
# 높이
for i in range(h):
    # 행
    for j in range(n):
        # 열
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

bfs()
res = []

# 맵을 확인하여 0이 있는지 체크 후, 가장 큰 값-1(경과 시간)이 정답
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            res.append(box[i][j][k])
print(max(res)-1)