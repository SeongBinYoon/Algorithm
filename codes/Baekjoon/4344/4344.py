# 평균은 넘겠지

import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    lst = list(map(int, input().split(' ')))
    num = lst[0]
    acc = 0
    for i in range(1, len(lst)):
        acc += lst[i]
    avg = acc / num
    
    cnt = 0
    for j in range(1, len(lst)):
        if lst[j] > avg:
            cnt += 1
    print(round(cnt / num * 100, 3),'%', sep='')