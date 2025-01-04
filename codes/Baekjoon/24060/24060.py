# 24060 알고리즘 수업 - 병합 정렬1

import sys
input = sys.stdin.readline

# lst를 오름차순으로 정렬
def merge_sort(lst, p, r):
    if p < r:
        q = (p + r) // 2                            # q = p와 r 중간 지점
        merge_sort(lst, p, q)                       # 전반부 정렬
        merge_sort(lst, q+1, r)                     # 후반부 정렬
        merge(lst, p, q, r)                         # 병합

# lst[p..q]와 lst[q+1...r]을 병합 -> lst[p...r]을 오름차순 정렬된 상태로 만든다.
# 각 lst[p..q]와 lst[q+1...r]은 오름차순으로 이미 정렬되어 있다.
def merge(lst, p, q, r):
    i, j = p, q+1
    tmp = []
    global cnt, ans
    # 두 개의 부분 첫번째 원소를 비교해 작은 것을 담는다.
    while(i <= q and j <= r):
        if lst[i] <= lst[j]:
            tmp.append(lst[i])
            i += 1
        else:
            tmp.append(lst[j])
            j += 1
    # 왼쪽 리스트가 남은 경우
    while i <= q:
        tmp.append(lst[i])
        i += 1
    # 오른쪽 리스트가 남은 경우
    while j <= r:
        tmp.append(lst[j])
        j += 1
    i, t = p, 0
    # 결과를 lst[p...r]에 저장
    while i <= r:
        lst[i] = tmp[t]
        cnt += 1
        if cnt == k:
            ans = lst[i]
            break
        i += 1
        t += 1

n, k = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
cnt, ans = 0, -1
merge_sort(lst, 0, n-1)
print(ans)