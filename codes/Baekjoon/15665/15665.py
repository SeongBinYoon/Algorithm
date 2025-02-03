# 15665 N과 M(11)

def backtracking():
    checker = 0
    if len(nodes) == m:
        print(' '.join(map(str, nodes)))
        return
    for i in range(n):
        # 같은 깊이의 중복 노드면 건너뜀
        if checker == lst[i]:
            continue
        # checker는 for내에 있으므로 같은 깊이의 중복 노드를 걸러줌
        checker = lst[i]
        nodes.append(lst[i])
        backtracking()
        nodes.pop()

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
# 노드를 담을 리스트
nodes = []
lst.sort()
backtracking()