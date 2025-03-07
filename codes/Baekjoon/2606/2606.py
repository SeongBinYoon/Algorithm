# 2606 바이러스

import sys
input = sys.stdin.readline
from collections import deque

# n=정점 수, m=간선 수
n = int(input())
m = int(input())
# 그래프 초기화 및 방문 리스트 생성
g = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

# 간선 내 정점 관계 그래프 추가
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

# 오름차순 정렬
for j in range(n+1):
    g[j].sort()

# bfs
def virus(g, start, visited):
    # 큐 생성
    queue = deque([start])
    # start 방문 처리
    visited[start] = 1
    while queue:
        # 큐에서 뽑기
        v = queue.popleft()
        for i in g[v]:
            if visited[i] == 0:
                # 큐에 추가
                queue.append(i)
                # 방문 처리
                visited[i] = 1
    return visited.count(1)

# 함수 호출 및 출력
print(virus(g, 1, visited)-1)