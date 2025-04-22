# 2667 단지번호붙이기

import sys
input = sys.stdin.readline
from collections import deque

# map 리스트, 결과 리스트
g, res = [], []
# 입력
n = int(input())
for _ in range(n):
    g.append(list(map(int, input().strip())))

# 상, 하
dx = [-1, 1, 0, 0]
# 좌, 우
dy = [0, 0, -1, 1]

# bfs
def bfs(g, a, b):
    # 큐 생성 및 (a, b) 쌍 삽입
    queue = deque([(a, b)])
    # 해당 위치 방문 처리
    g[a][b] = 0
    cnt = 1
    # queue 비울 때까지
    while queue:
        # 큐에서 좌표 꺼내기
        x, y = queue.popleft()
        # 꺼낸 좌표에서 상,하,좌,우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 벽으로 막혀있는 경우, 다음 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 방문하지 않은 경우
            if g[nx][ny] == 1:
                # 큐에 삽입
                queue.append((nx, ny))
                # 방문 처리
                g[nx][ny] = 0
                # cnt+1
                cnt += 1
    # 끝나면 cnt 값 return
    return cnt

# 모든 행, 열을 돌며 방문하지 않은 곳을 시작점으로 호출
for i in range(n):
    for j in range(n):
        # 방문하지 않은 경우
        if g[i][j] == 1:
            res.append(bfs(g, i, j))

# 결과 출력
# 각 단지 내 집 수 오름차순 정렬
res.sort()
print(len(res))
for k in range(len(res)):
    print(res[k])