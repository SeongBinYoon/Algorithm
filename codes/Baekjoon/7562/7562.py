# 7562 나이트의 이동

import sys
input = sys.stdin.readline
from collections import deque

# 이동(8방향)
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# bfs
def bfs(g, a, b, t1, t2):
    # 큐 생성 및 시작점 튜플 삽입
    queue = deque()
    queue.append((a, b))
    # 시작점 방문 처리
    g[a][b] = 1
    # 큐가 빌 때까지
    while queue:
        # 꺼냄
        x, y = queue.popleft()
        # 시작점이 목표 지점인 경우
        if x == t1 and y == t2:
            return 0
        # 이동
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계선 벗어나면 넘김
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            # 목표 지점인 경우
            if nx == t1 and ny == t2:
                return g[x][y]
            # 방문하지 않은 경우
            if g[nx][ny] == 0:
                # 큐 삽입
                queue.append((nx, ny))
                # 방문 처리
                g[nx][ny] = g[x][y] + 1

# 테스트 케이스 개수
n = int(input())
for _ in range(n):
    # 체스판 한 변의 길이
    l = int(input())
    # 나이트 현재 칸
    a, b = map(int, input().split())
    # 나이트의 목표 칸
    t1, t2 = map(int, input().split())
    # 맵 생성
    g = [[0 for _ in range(l)] for _ in range(l)]
    # 함수 호출
    print(bfs(g, a, b, t1, t2))