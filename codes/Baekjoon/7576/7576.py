# 7576 토마토

import sys
input = sys.stdin.readline
from collections import deque

box = []
m, n = map(int, input().split())                # 6,4
for _ in range(n):
    box.append(list(map(int, input().split())))

# 좌우
dx = [-1, 1, 0, 0]
# 상하
dy = [0, 0, -1, 1]

# 큐 선언
queue = deque()

# bfs
def bfs():
    # 큐가 빌 때까지 반복
    while queue:
        # 꺼냄(x행, y열)
        x, y = queue.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계선 밖이면 다시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # -1이면(들어있지 않은 칸) 다시
            if box[nx][ny] == -1:
                continue
            # 0이면(익지 않은 곳)
            if box[nx][ny] == 0:
                # 1로 방문 처리(익음)
                box[nx][ny] = box[x][y] + 1
                # 큐 삽입
                queue.append((nx, ny))

# 행과 열을 돌며 1인 곳을 시작점으로 큐에 삽입
for i in range(n):          # 4번
    for j in range(m):      # 6번
        if box[i][j] == 1:
            queue.append([i, j])

bfs()
res = []

# 맵을 확인하여 0이 있는지 체크 후, 가장 큰 값-1(경과 시간)이 정답
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        res.append(box[i][j])
print(max(res)-1)

'''
# 그래프 확인용
print()
for _ in range(len(box)):
    print(*box[_])
'''