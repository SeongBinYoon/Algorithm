# 9012 괄호

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    flag = 0
    stack = []
    stack.clear()
    lst = list(map(str, input().strip()))
    for i in range(len(lst)):
        # '('일 때
        if lst[i] == '(':
            stack.append(1)
        # ')'일 때
        else:
            # 스택이 비어 있으면
            if len(stack) == 0:
                # flag 1로, break
                flag = 1
                break
            # 스택이 비어 있지 않으면
            else:
                stack.pop()
    # flag = 0인 것은 무사히 순서를 지켜 수행된 것
    if flag == 0:
        # 끝난 후 남은게 없으면 VPS
        if len(stack) == 0:
            print("YES")
        # 끝난 후 남은게 있으면
        else:
            print("NO")
    # flag = 1인 것은 아무것도 없는데 pop한 경우
    else:
        print("NO")