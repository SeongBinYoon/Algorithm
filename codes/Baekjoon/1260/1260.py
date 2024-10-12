# 1260 DFS와 BFS

from collections import deque

def dfs(g, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in g[v]:
        if visited[i] == False:
            dfs(g, i, visited)

def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in g[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split(' '))
g = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split(' '))
    if b not in g[a]:
        g[a].append(b)
    if a not in g[b]:
        g[b].append(a)
for j in range(n+1):
    g[j].sort()

# print(g)
visited = [False] * (n+1)
dfs(g, v, visited)
print()
visited = [False] * (n+1)
bfs(g, v, visited)