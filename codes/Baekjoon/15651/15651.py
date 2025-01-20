# 15651 N과 M(3)

def backtracking():
    # 수열이 완성되면
    if len(res) == m:
        # 출력
        print(' '.join(map(str, res)))
        return
    # 모든 자식 노드에 대해
    for i in range(1, n+1):
        # 중복 조건 없이 수행
        res.append(i)
        backtracking()
        res.pop()

n, m = map(int, input().split(' '))
# 수열을 담을 공유 리스트
res = []
backtracking()