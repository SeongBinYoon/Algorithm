# 5568 카드 놓기

# 백트래킹 알고리즘
def card():
    # 종료조건
    if len(nodes) == k:
        target = ''.join(map(str, nodes))
        # if target not in res:
        res.add(target)
        return
    for i in range(len(lst)):
        # 동일한 자리의 수는 제외
        if visited[i]:
            continue
        visited[i] = 1
        nodes.append(lst[i])
        card()
        visited[i] = 0
        nodes.pop()

lst, nodes, res = [], [], set([])
n = int(input())
k = int(input())
for _ in range(n):
    c = input()
    lst.append(c)
# 자기자신은 제외하되, 중복된 다른 수는 돌도록
visited = [0] * n
card()
# print(res)
print(len(res))