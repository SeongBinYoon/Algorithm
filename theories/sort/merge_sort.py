# 합병 정렬(Merge sort, O(nlogn))
# BOJ #24060

# Test code
# 32 23 17 5 11 99 55

def mergeSort(xs):
    if len(xs) > 1:
        mid = len(xs) // 2
        return merge(mergeSort(xs[:mid]), mergeSort(xs[mid:]))
    else:
        return xs

def merge(left, right):
    # 둘 다 비어있지 않으면
    if not (left == [] or right == []):
        # left가 작을 때 두 개의 첫번째 원소 비교
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:], right)
        else:
            return [right[0]] + merge(left, right[1:])
    else:
        return left + right

lst = list(map(int, input().split(' ')))
print(mergeSort(lst))