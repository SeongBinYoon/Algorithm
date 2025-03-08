# 1012 유기농 배추

import sys
input = sys.stdin.readline
from collections import deque

# 상, 하
dx = [-1, 1, 0, 0]
# 좌, 우
dy = [0, 0, -1, 1]

# bfs
def bfs(g, a, b):
    # 큐 생성 및 시작점 삽입
    queue = deque([(a,b)])
    # 방문 처리
    g[a][b] = 0
    # 카운팅
    cnt = 1
    # 큐 비울 때까지
    while queue:
        # 큐에서 뽑기
        x, y = queue.popleft()
        # 상, 하, 좌, 우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 벽으로 막혀있는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 방문하지 않은 경우
            if g[nx][ny] == 1:
                # 큐에 삽입
                queue.append((nx, ny))
                # 방문 처리
                g[nx][ny] = 0
                # 카운팅
                cnt += 1
    return cnt

# 입력
t = int(input())
for _ in range(t):
    # 결과 리스트
    res = []
    # 가로길이(열), 세로길이(행), 배추 위치 개수
    m, n, k = map(int, input().split())
    # 그래프 생성
    g = [[0 for _ in range(m)] for _ in range(n)]
    # k번 입력
    for _ in range(k):
        y, x = map(int, input().split())
        g[x][y] = 1
    # 함수 호출
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                res.append(bfs(g, i, j))
    # 결과 출력
    print(len(res))