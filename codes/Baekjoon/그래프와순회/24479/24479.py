# 24479 알고리즘 수업-깊이 우선 탐색 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# n=정점 수, m=간선 수, r=시작정점
n, m, r = map(int, input().split())
# 그래프, 방문 정보 초기화
g = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
# 순서 변수
cnt = 0

# 간선 수 만큼 반복
for _ in range(m):
    u, v = map(int, input().split())
    g[v].append(u)
    g[u].append(v)

# 오름차순 정렬
for j in range(n+1):
    g[j].sort()

# dfs
def dfs(g, v, visited):
    global cnt
    # 순서+1, 방문 여부에 순서 저장
    cnt += 1
    visited[v] = cnt
    # v번째 리스트를 돌며 방문하지 않았으면 i번째 리스트로 재귀
    for i in g[v]:
        if visited[i] == 0:
            dfs(g, i, visited)

# 호출 및 출력
dfs(g, r, visited)
for i in range(1, len(visited)):
    print(visited[i])