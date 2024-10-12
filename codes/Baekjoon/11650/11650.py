# 11650 좌표 정렬하기

# 버블 정렬(O(n^2))로 풀면 시간초과가 발생한다.
# sorted를 사용해 통과했는데, sorted, sort는 시간복잡도가 퀵 정렬(O(nlogn))보다 작다고 한다.
# 왠만하면 시험 문제에서는 sort, sorted를 사용하자. (각 정렬 원리도 숙지할 것)

import sys
sys.stdin.readline

lst = []
box = []
n = int(input())
# 입력 받아 이중 리스트 저장
for _ in range(n):
    x, y = map(int, input().split())
    box.append(x)
    box.append(y)
    lst.append(box)
    box = []

'''
# 버블 정렬 (bubble sort) -> 시간복잡도가 높아 시간초과 발생
for i in range(n-1):
    for j in range(n-i-1):
        # 앞의 x좌표가 크면 뒤로
        if lst[j][0] > lst[j+1][0]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
        # 앞의 x좌표가 같으면 y좌표를 살핀다
        elif lst[j][0] == lst[j+1][0]:
            # 앞의 y좌표가 크면 뒤로
            if lst[j][1] > lst[j+1][1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
'''
lst = sorted(lst)

# 출력
for k in range(n):
    for l in range(2):
        print(lst[k][l], end=' ')
    print()