# 11724 연결 요소의 개수

import sys
input = sys.stdin.readline
from collections import deque

# n=정점 개수, m=간선 개수
n, m = map(int, input().split())
# 그래프 선언
g = [[] for _ in range(n+1)]
# 방문 여부 리스트
visited = [0 for _ in range(n+1)]
# 관계 그래프 채우기
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

# 연결 개수
cnt = 0

# bfs
def bfs(g, start, visited):
    # 큐 생성 및 시작점 삽입
    queue = deque()
    queue.append(start)
    # 방문 처리
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

# 방문 리스트 돌며 bfs 수행
for k in range(1, n+1):
    # 방문하지 않았으면 새로운 연결 시작점
    if visited[k] == 0:
        bfs(g, k, visited)
        cnt += 1
print(cnt)