# 3273 두 수의 합

import sys
input = sys.stdin.readline

# 입력
n = int(input())
lst = list(map(int, input().split()))
x = int(input())

# 정렬
lst.sort()

# 투 포인터 알고리즘
left, right = 0, n-1
cnt = 0
# 두 포인터가 역전되면 종료
while left < right:
    acc = lst[left] + lst[right]
    # 목표와 같으면 카운트, 두 포인터는 서로 다가감
    if acc == x:
        cnt += 1
        left += 1
        right -= 1
    # 합이 목표보다 작으면 왼쪽 포인터 이동
    elif acc < x:
        left += 1
    # 합이 목표보다 크면 오른쪽 포인터 이동
    else:
        right -= 1
print(cnt)