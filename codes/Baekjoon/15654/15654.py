# 15654 N과 M(5)

def backtracking():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    # 제시된 리스트를 돌며
    for s in lst:
        # 중복 방지
        if s not in res:
            res.append(s)
            backtracking()
            res.pop()

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
lst.sort()
res = []
backtracking()