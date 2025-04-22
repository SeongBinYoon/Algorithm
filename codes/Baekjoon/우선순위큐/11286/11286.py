# 11286 절댓값 힙

import sys, heapq
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
    x = int(input())
    # x가 0이면
    if x == 0:
        # 비어있으면 0 출력
        if len(heap) == 0:
            print(0)
        # 비어있지 않으면
        else:
            print(heapq.heappop(heap)[1])
    # x가 0이 아니면
    else:
        # <우선순위, 값> 튜플 형태로 삽입
        heapq.heappush(heap, (abs(x), x))