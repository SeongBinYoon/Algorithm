# 2164 카드2

'''
# 스택 -> 시간초과
n = int(input())
lst = [i for i in range(1, n+1)]
for _ in range(n-1):
    # 제일 위 카드를 버린다.
    lst = lst[1:]
    # 다음 카드를 제일 아래로(뒤로) 옮긴다.
    lst.append(lst[0])
    # lst 최신화
    lst = lst[1:]
    # print(lst)
# 마지막 남은 카드 출력
print(lst[0])
'''

# 덱 -> 통과
from collections import deque

n = int(input())
# 덱 선언
dq = deque([i for i in range(1, n+1)])
for _ in range(n-1):
    dq.popleft()        # 왼쪽 카드 버림
    dq.rotate(-1)       # 왼쪽(음수)으로 회전
print(dq[0])            # 덱에 마지막 남은 수 출력