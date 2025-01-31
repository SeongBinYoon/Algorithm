# 16922 로마 숫자 만들기

# 백트래킹 알고리즘
def roman():
    if len(nodes) == n:
        # if sum(nodes) not in res:
        res.add(sum(nodes))
        return
    for s in lst:
        if len(nodes) == 0:
            nodes.append(s)
            roman()
            nodes.pop()
        elif len(nodes) != 0 and s >= max(nodes):
            nodes.append(s)
            roman()
            nodes.pop()

n = int(input())
# 주어진 수, 각 노드를 담을 리스트, n개 숫자를 합한 결과 리스트(중복 없음)
lst, nodes, res = set([1, 5, 10, 50]), [], set([])
roman()
print(len(res))