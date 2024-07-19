# 9506 약수들의 합

import sys
input = sys.stdin.readline

acc = 0
lst = []

while True:
    n = int(input())
    # 종료 조건
    if n == -1:
        break
    # 받은 n의 약수를 확인
    for i in range(1, n):
        # 약수라면
        if n % (i) == 0:
            acc += (i)
            lst.append(i)
    # 완전수라면
    if acc == n:
        print(f"{n} = ", end='')
        # 리스트를 돌며 약수 출력
        for j in range(len(lst)):
            print(lst[j], end=' ')
            if j != len(lst) - 1:
                print('+', end=' ')
            else:
                print()
    # 완전수가 아니라면
    else:
        print(f"{n} is NOT perfect.")
    # 변수 초기화
    acc = 0
    lst = []