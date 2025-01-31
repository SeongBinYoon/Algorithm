# 10974 모든 순열

def backtracking():
    if len(res) == n:
        print(' '.join(map(str, res)))
        return
    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            backtracking()
            res.pop()

n = int(input())
res = []
backtracking()