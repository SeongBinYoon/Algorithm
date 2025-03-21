# 11725 트리의 부모 찾기

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 그래프 선언
g = [[] for _ in range(n+1)]
# 방문 여부 리스트
visited = [0 for _ in range(n+1)]
# 관계 그래프 생성
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
# 오름차순 정렬
for j in range(n+1):
    g[j].sort()
# print(g)              #[[], [4, 6], [4], [5, 6], [1, 2, 7], [3], [1, 3], [4]]

# 각 인덱스(노드)별 부모 저장 리스트
res = [0 for _ in range(n+1)]

# bfs
def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if visited[i] == 0:
                queue.append(i)
                # 부모 노드 저장
                res[i] = v
                visited[i] = 1

bfs(g, 1, visited)

# 출력
for k in range(2, n+1):
    print(res[k])