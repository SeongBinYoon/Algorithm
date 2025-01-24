# 15655 N과 M(6)

def backtracking():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    # 모든 노드에 대해 수행
    for s in lst:
        # 중복 방지
        if s not in res:
            # 처음 들어가는 수는 무조건 수행
            if len(res) == 0:
                res.append(s)
                backtracking()
                res.pop()
            # 두번째 노드부터는 최대 수보다 커야 추가 - 중복된 수열 발생 방지
            elif len(res) != 0 and s > max(res):
                res.append(s)
                backtracking()
                res.pop()

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
lst.sort()
res = []
backtracking()