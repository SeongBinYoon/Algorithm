# 9663 N-Queen

import sys
input = sys.stdin.readline

cnt = 0
lst = []

def nqueen(rowcnt):
    global cnt              # 방법 가지 수 - 전역변수로 선언

    # 행 번호가 n에 다다르면 종료, return으로 재귀 함수 종료 후 바로 전 함수에서 pop 수행
    if rowcnt == n:
        cnt += 1
        # print(lst)
        return
    
    # 열을 선택하는 반복문
    for i in range(1, n+1):
        # 건너뛰는 조건: continue로 다음 코드 수행하지 않고 for문으로 돌아감
        # 1. lst에 존재하는 경우
        # lst의 수가 1, 3인 경우 i가 1, 3이 될 수 없음 (아래, 직선)
        # 2. 두 퀸((rowcnt, i)와 (j, lst[j]))의 행 간 차(rowcnt-j)와 열 간 차(i-lst[j])가 같으면 대각선에 위치함
        # lst의 마지막 수가 3인 경우 i가 2,4가 될 수 없음 (좌우대각선)
        if i in lst or any(abs(rowcnt - j) == abs(i - lst[j]) for j in range(len(lst))):
            continue

        lst.append(i)
        nqueen(rowcnt+1)
        # n개에 다다르면 위 if 조건에서 return되어 pop 수행
        # n개에 다다르지 못하면 해당 for문에서 모두 돌고 종료되며 pop 수행
        lst.pop()

n = int(input())
nqueen(0)
print(cnt)