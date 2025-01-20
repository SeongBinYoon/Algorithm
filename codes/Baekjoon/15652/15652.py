# 15652 N과 M(4)

def backtracking():
    # 수열이 완성되면
    if len(res) == m:
        # 출력
        print(' '.join(map(str, res)))
        return
    # 모든 자식 노드에 대해
    for i in range(1, n+1):
        # 중복 조건 없이 수행
        # 첫 노드면 수행
        if len(res) == 0:
            res.append(i)
            backtracking()
            res.pop()
        # 첫 노드가 아니고 수열에서 가장 큰 것보다 커야 수행
        elif len(res) != 0 and i >= max(res):
            res.append(i)
            backtracking()
            res.pop()

n, m = map(int, input().split(' '))
# 수열을 담을 공유 리스트
res = []
backtracking()