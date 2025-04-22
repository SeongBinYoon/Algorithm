# 2559 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))

# 누적 합 리스트
for i in range(1, n):
    lst[i] = lst[i-1] + lst[i]
# 연속 합 리스트
findmax = [lst[k-1]]

# 기존 리스트: 3,-2,-4,-9,0,3,7,13,8,-3
# 누적 합 리스트: 3,1,-3,-12,-12,-9,-2,11,19,16
# 누적 합 리스트의 k-1번째가 연속 합 리스트의 첫번째 값 (n=10, k=2인 경우 1)
# 연속 합 리스트 j번 인덱스의 값 = 누적 합 리스트의 j번째 값 - j-k번째 값
for j in range(k, n):
    findmax.append(lst[j] - lst[j-k])
print(max(findmax))