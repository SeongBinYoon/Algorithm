# 15656 N과 M(7)

def backtracking():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    # 모든 노드에 대해 수행
    for s in lst:
        # 중복 조건 없음, 오름차순 조건 없음
        res.append(s)
        backtracking()
        res.pop()

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
lst.sort()
res = []
backtracking()