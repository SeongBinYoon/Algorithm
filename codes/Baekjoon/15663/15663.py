# 15663 N과 M(9)

def backtracking():
    checker = 0
    if len(nodes) == m:
        print(' '.join(map(str, nodes)))
        return
    for i in range(n):
        if visited[i] or checker == lst[i]:
            continue
        visited[i] = 1
        # checker는 for내에 있으므로 같은 깊이의 중복 노드를 걸러줌
        checker = lst[i]
        nodes.append(lst[i])
        backtracking()
        visited[i] = 0
        nodes.pop()

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
# 방문한 부모노드와의 중복을 방지, 노드를 담을 리스트
visited, nodes = [0] * n, []
lst.sort()
backtracking()