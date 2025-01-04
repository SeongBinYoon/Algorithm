# 5430 AC
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    # 명령어
    p = deque(input().strip('\n'))
    # 리스트에 들어있는 수 개수
    n = int(input())
    # 리스트
    lst = input().strip('\n')
    # 오름차순=0, 내림차순=1
    flag = 0
    # 에러코드
    error = 0
    # 대괄호 및 콤마 
    lst = lst[1:-1].split(',')
    for i in range(n):
        lst[i] = int(lst[i])
    
    lst = deque(lst)
    # 명령어가 끝날 때까지 반복
    while len(p) != 0:
        # 수의 순서를 뒤집기
        if p[0] == 'R':
            # 오름차순 되어있을 때 R인 경우
            if flag == 0:
                flag = 1
            # 내림차순 되어있을 때 R인 경우
            else:
                flag = 0
        # 첫번째 수 버리기
        elif p[0] == 'D':
            # 비어있으면 에러 출력
            if len(lst) == 0 or lst[0] == '':
                print("error")
                error = 1
                break
            else:
                if flag == 0:
                    lst.popleft()
                else:
                    lst.pop()
        # 명령어 최신화
        p.popleft()
    
    # error 아닌 경우 다음 출력
    if error == 0:
        print('[', end='')
        # reverse된 상태면 뒤집고 출력
        if flag == 1:
            lst.reverse()
        if len(lst) == 0:
            print("]")
        else:
            for i in range(len(lst)):
                if i == len(lst)-1:
                    print(lst[i], end='')
                    print(']')
                else:
                    print(lst[i], end=',')