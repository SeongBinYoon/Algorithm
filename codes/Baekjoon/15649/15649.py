# 15649 N과 M(1)

def backtracking():
    # 수열이 완성되면
    if len(res) == m:
        # 출력
        print(" ".join(map(str, res)))
        return
    # 모든 자식 노드에 대해
    for i in range(1, n+1):
        # 정답에 유망하다면(답의 가능성이 있다면) = 수열에 i가 없다면
        if i not in res:
            res.append(i)           # 자식노드로 이동 = 수열에 추가
            backtracking()          # 재귀함수
            res.pop()               # 부모노드로 이동 = 재귀함수 호출 후 return되면 여기로 돌아와 하나씩 제거
                                    # 1,2,3이면 3을 제거해 1,2인 부모노드로 이동
                                    
n, m = map(int, input().split(' '))
# 수열을 담을 공유 리스트
res = []
backtracking()


'''
# Python 내장 함수 방법 - 메모리는 동일, 속도는 위 백트래킹 알고리즘보다 빠름
from itertools import permutations
n, m = map(int, input().split(' '))
p = permutations(range(1, n+1), m)
for i in p:
    print(" ".join(map(str, i)))
'''