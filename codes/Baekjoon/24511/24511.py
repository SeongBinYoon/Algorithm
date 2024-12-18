# 24511 queuestack

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())                                        # 4
queuestack = list(map(int, input().split(' ')))         # 0 1 1 0
element = deque(map(int, input().split(' ')))           # 1 2 3 4
circle = int(input())                                   # 3
new = list(map(int, input().split(' ')))                # 2 4 7

# 이 문제는 스택과 큐의 작동 방식을 깊이 이해해야 한다.
# 스택인 경우 결국 담긴 수는 쓰이지 않고 넘어온 수가 다음 큐로 추가된다.
# 즉, 스택은 고려할 필요가 없다. 0(큐)인 것만 일렬로 세워두고 생각하면 된다.
# 이 경우, 두 개의 큐에 1과 2가 각각 들어가 있고, 3, 4를 입력한다고 가정하면
# 첫번째 circle에서 답은 2가 되고, 두 개의 큐에는 3, 1이 담긴다.
# 두번째 circle에서 답은 1이 되고, 두 개의 큐에는 4, 3이 담긴다.
# 입력 개수만큼 돌며 가장 마지막 큐에 담겨있는 수가 답이 되고, 입력 수는 큐의 맨 앞에 추가되는 방식이다.

# 자료구조가 큐인 것만 뽑아 새로운 덱 생성
new_element = deque(element[i] for i in range(n) if queuestack[i] == 0)
# 전부 1(스택)인 경우, 입력 그대로 출력
if len(new_element) == 0:
    for s in new:
        print(s, end=' ')
# 자료구조에 0(큐)가 존재하는 경우 다음 수행
else:
    # 입력받는 만큼 반복
    for j in range(circle):
        # 덱의 마지막 수 출력
        print(new_element[-1], end=' ')
        # 덱의 마지막 수 제거
        new_element.pop()
        # 덱의 앞에 입력 수 추가
        new_element.appendleft(new[j])

'''
# 시간 초과 -> 모든 동작을 구현할 필요 없다.
# circle번(입력 개수만큼) 반복
for i in range(circle):
    # 대기열은 한 circle마다 초기화
    standby = []
    # 자료구조 개수만큼 반복
    for j in range(n):
        # 대기열이 공백일 때(첫 circle일 때)
        if standby == []:
            # j번째 자료구조가 스택이면 element 그대로, new의 i번째는 대기열로
            if queuestack[j] == 1:
                standby.append(new[i])
            # j번째 자료구조가 큐면 기존 element j번째(1번째)는 대기열로, new의 i번째가 element 1번째로
            else:
                standby.append(element[j])
                element[j] = new[i]
        # 대기열이 공백이 아닐 때(이후 circle부터)
        else:
            # j번째 자료구조가 스택이면 element 그대로, 대기열의 이전 인덱스 그대로
            if queuestack[j] == 1:
                standby.append(standby[j-1])
            # j번째 자료구조가 큐면 기존 element의 수를 대기열로, 대기열 마지막 수(이전 수)를 element로
            else:
                standby.append(element[j])
                element[j] = standby[j-1]
    # print(element)
    # print(standby)
    # print()
    print(standby[-1], end=' ')
'''