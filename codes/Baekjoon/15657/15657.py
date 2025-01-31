# 15657 N과 M(8)

def backtracking():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    # 모든 노드에 대해 수행
    for s in lst:
        # 중복 조건 없음, 비내림차순
        # 첫 노드는 무조건 추가
        if len(res) == 0:
            res.append(s)
            backtracking()
            res.pop()
        # 두번째 노드부터는 리스트의 최대 수보다 같거나 크면 추가
        elif len(res) != 0 and s >= max(res):
            res.append(s)
            backtracking()
            res.pop()

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
lst.sort()
res = []
backtracking()