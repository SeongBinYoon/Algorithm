# depth-first search algorithm (깊이 우선 탐색 알고리즘)

# 1. 탐색 시작 노드를 스택에 넣고 방문처리
# 2. 스택 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있다면 그 노드를 스택에 넣고 (보통 가장 작은 노드) 방문처리
# 방문하지 않은 인접 노드가 없다면 (모두 방문했다면) 스택에서 최상단 노드를 꺼냄
# 3. 2번을 수행할 수 없을 때까지 반복

def dfs(g, v, visited):

    visited[v] = True   # 탐색 시작 노드 스택에 넣고 방문처리
    print(v, end=' ')   # 출력
    for i in g[v]:      # graph의 1번 노드와 이어진 노드를 하나씩 확인
        if visited[i] == False:     # 방문하지 않았으면 재귀 호출
            dfs(g, i, visited)

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
dfs(g, 1, visited) # v=1번 노드부터 시작