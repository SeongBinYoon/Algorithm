# 15664 N과 M(10)

def backtracking():
    checker = 0
    if len(nodes) == m:
        print(' '.join(map(str, nodes)))
        return
    for i in range(n):
        # 부모 노드와 겹치거나, 같은 깊이의 중복 노드거나, 첫 수행이 아닐 때 비내림차순이 아니면 건너뜀
        if visited[i] or checker == lst[i] or (len(nodes) != 0 and lst[i] < max(nodes)):
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