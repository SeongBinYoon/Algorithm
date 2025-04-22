# 2206 벽 부수고 이동하기

import sys
input = sys.stdin.readline
from collections import deque

# 그래프 및 입력
g = []
n, m = map(int, input().split())
for _ in range(n):
    g.append(list(map(int, input().strip())))

# 방문 여부 리스트(벽 부수지 않음=0, 벽 부숨=1)
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

# 뱡향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))
    # 시작점 방문처리
    visited[a][b][c] = 1
    while queue:
        x, y, z = queue.popleft()
        # 종점에 도달했을 경우
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이동할 곳이 벽이고 z가 0(벽 부수지 않음)인 경우
            if g[nx][ny] == 1 and z == 0:
                # 벽을 부수고(큐에 z=1삽입) 방문처리
                visited[nx][ny][1] = visited[x][y][0] + 1
                # 이 좌표의 벽은 부숨(1)
                queue.append((nx, ny, 1))
            # 이동할 곳이 벽이 아니고 방문하지 않은 곳인 경우
            elif g[nx][ny] == 0 and visited[nx][ny][z] == 0:
                # 방문처리 및 큐 삽입
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            # 이동할 곳이 벽이고 벽을 이미 부순 경우, 벽이 아니고 방문한 경우는 건너뜀
    return -1

print(bfs(0,0,0))
# print(visited)