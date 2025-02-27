# 2217 로프

import sys
input = sys.stdin.readline

lst, res = [], []
n = int(input())
for _ in range(n):
    lst.append(int(input()))
# 내림차순 정렬
lst = sorted(lst, reverse=True)
# 모든 로프를 사용하지 않을 때도 고려해야 함
# 내림차순으로 정렬된 리스트에서 각 요소 x 인덱스 번호(사용되는 로프 개수)가 최대중량이 됨
for i in range(n):
    res.append(lst[i] * (i+1))
# 그 중 최댓값 출력
print(max(res))