# 네트워크

def solution(n, computers):
    answer = 0
    # 방문 리스트
    visited = [False for _ in range(n)]
    
    # computers 내의 각 리스트를 확인
    for i in range(n):
        if visited[i] == False:
            # dfs 원리로 타고 타고 들어감, i = 0, 1, 2
            dfs(computers, i, visited)
            # 연결이 끊어지면 +1
            answer += 1
    return answer

def dfs(g, v, visited):
    # 타고 들어왔으면 방문처리, v = 0
    visited[v] = True
    # 안의 리스트의 값 확인, j = 1, g[v] = [1, 1, 0]
    for j in range(len(g[v])):
        # 자기 자신이 아니고, 1이면서 방문하지 않았으면 재귀호출
        if j != v and g[v][j] == 1 and not visited[j]:
            dfs(g, j, visited)