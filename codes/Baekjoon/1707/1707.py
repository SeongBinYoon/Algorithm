# 1707 이분 그래프

import sys
input = sys.stdin.readline
from collections import deque

# bfs
def bfs(g, start, visited):
    queue = deque([start])
    # 방문 처리
    visited[start] = 1
    while queue:
        v = queue.popleft()
        # print(v)
        for i in g[v]:
            # 방문하지 않았다면
            if visited[i] == 0:
                queue.append(i)
                # 상위 노드와 다른 그룹으로
                visited[i] = -1 * visited[v]
            # 이미 방문했는데 같은 그룹이라면
            elif visited[i] == visited[v]:
                # 이분 그래프가 아님
                return False
    # 끝까지 문제없이 수행되면 이분 그래프
    return True

# 입력
# t=테스트케이스 개수
t = int(input())
for _ in range(t):
    # v=정점 개수, e=간선 개수
    v, e = map(int, input().split())
    # 관계 그래프 생성
    g = [[] for _ in range(v+1)]
    # 방문 여부 리스트
    visited = [0 for _ in range(v+1)]
    for _ in range(e):
        # u,v=두 정점의 번호
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    # 연결이 끊긴 부분에 대한 수행
    for i in range(1, v+1):
        # 방문한 노드가 아니면 bfs 수행
        if not visited[i]:
            res = bfs(g, i, visited)
            if not res:
                break
    print("YES" if res else "NO")