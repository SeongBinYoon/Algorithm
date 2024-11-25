# 28278 스택2

import sys
input = sys.stdin.readline


stack = []
n = int(input())
for _ in range(n):
    c = list(map(int, input().split(' ')))
    # 앞 수가 1이면 뒤 수 삽입
    if c[0] == 1:
        stack.append(c[1])
        # print(stack)
    # 앞 수가 2이면
    elif c[0] == 2:
        # 스택이 비어 있으면 -1 출력
        if len(stack) == 0:
            print(-1)
            # print(stack)
        # 스택이 비어 있지 않다면
        else:
            # 맨 위 정수 빼고 출력
            print(stack[-1])
            stack.pop()
            # print(stack)
    # 앞 수가 3이면 스택에 들어있는 정수(스택의 길이) 출력
    elif c[0] == 3:
        print(len(stack))
        # print(stack)
    # 앞 수가 4이면
    elif c[0] == 4:
        # 스택이 비어 있으면 1 출력
        if len(stack) == 0:
            print(1)
            # print(stack)
        # 스택이 비어 있지 않으면 0 출력
        else:
            print(0)
            # print(stack)
    # 앞 수가 5이면 맨 위의 정수 출력
    else:
        if len(stack) == 0:
            print(-1)
            # print(stack)
        else:
            print(stack[-1])
            # print(stack)