# breadth-first search algorithm (너비 우선 탐색 알고리즘)

# 1. 탐색 초기 노드를 큐에 넣고 방문처리
# 2. 큐에서 노드 꺼내고 이 노드 인접 노드 중 방문하지 않은 노드를 모두 큐에 넣고 방문처리
# 3. 2번을 수행할 수 없을 때까지 반복

from collections import deque

def bfs(g, start, visited):
    queue = deque([start])  #탐색 초기 노드 큐에 넣음
    visited[start] = True   # 방문처리
    while queue:            # queue에 아무것도 없을 때까지 반복
        v = queue.popleft() # 큐에서 노드 꺼냄
        print(v, end=' ')   # 출력
        
        for i in g[v]:      # 꺼낸 노드의 인접 노드 확인
            if visited[i] == False:     # 방문하지 않았으면
                queue.append(i)         # 큐에 넣음
                visited[i] = True       # 방문처리
                                        # 방문했으면 무시

g = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(g, 1, visited) # v=1번 노드부터 시작