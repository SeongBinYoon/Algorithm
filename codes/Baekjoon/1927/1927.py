# 1927 최소 힙

import sys, heapq
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
    x = int(input())

    # 0이면 가장 작은 값 출력
    if x == 0:
        # 비어있으면 0 출력
        if len(heap) == 0:
            print(0)
        # 비어있지 않으면
        else:
            print(heapq.heappop(heap))
    # 0이 아니면 x 삽입
    else:
        heapq.heappush(heap, x)