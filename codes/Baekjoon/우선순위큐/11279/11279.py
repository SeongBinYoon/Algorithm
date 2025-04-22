# 11279 최대 힙

import sys, heapq
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
    x = int(input())

    # 0이면 가장 큰 값 출력
    if x == 0:
        # 비어있으면 0 출력
        if len(heap) == 0:
            print(0)
        # 비어있지 않으면 가장 큰 값 출력
        else:
            print(heapq.heappop(heap)[1])

    # 0이 아니면 x 삽입
    else:
        # 튜플로 우선순위 생성
        heapq.heappush(heap, (-x, x))