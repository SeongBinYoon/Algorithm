# 1874 스택 수열

import sys
input = sys.stdin.readline

# 입력받은 수열, 1~n 리스트, 스택, 결과값 리스트
lst, order, stack, res = [], [], [], []

# 수열 입력
n = int(input())
for _ in range(n):
    lst.append(int(input().strip()))

# 1~n 리스트
order = [i for i in range(1, n+1)]

def solution(order, lst):
    # 갱신 시 슬라이싱-O(n), 인덱스 접근-O(1)이므로 인덱스를 초기화
    l, o = 0, 0
    # 수열 리스트를 모두 돌면 종료
    while l != n:
        # stack 체크 - stack에 있으면
        if lst[l] in stack:
            # 바로 전이 아니라면 NO
            if stack[-1] != lst[l]:
                print('NO')
                exit(0)
            # 바로 전이라면 올바른 수열
            else:
                # pop
                stack.pop()
                res.append('-')
                # lst 갱신
                l += 1
        # stack 체크 - stack에 없으면
        else:
            # 일단 push
            stack.append(order[o])
            res.append('+')
            # order 갱신
            o += 1
    return res

# 함수 호출 및 출력
solution(order, lst)
for i in range(len(res)):
    print(res[i])