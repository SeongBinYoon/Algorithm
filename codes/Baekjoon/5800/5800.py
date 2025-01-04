# 5800 성적 통계

import sys
input = sys.stdin.readline

k = int(input())
for i in range(1, k+1):
    lst = list(map(int, input().split(' ')))
    n = lst[0]
    lst = lst[1:]
    tmp = []
    # max, min 찾기
    maxval = max(lst)
    minval = min(lst)
    # gap 찾기
    lst = sorted(lst, reverse=True)
    for j in range(n-1):
        tmp.append(lst[j] - lst[j+1])
    gap = max(tmp)
    print("Class", i)
    print(f"Max {maxval}, Min {minval}, Largest gap {gap}")