# 1697 숨바꼭질

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

# 0<=n,k<=100000이므로
visited = [0 for _ in range(100001)]

def bfs(start, k):
    queue = deque([start])
    visited[start] = 1
    # 시작점과 목표점이 같은 경우
    if start == k:
        return 0
    while queue:
        x = queue.popleft()
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            # 경계선 넘어가면 넘김
            if nx < 0 or nx >= 100001:
                continue
            # 해당 값이면 리턴
            if nx == k:
                return visited[x]
            # 방문하지 않았으면 이전 값 +1
            if visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] + 1

print(bfs(n, k))