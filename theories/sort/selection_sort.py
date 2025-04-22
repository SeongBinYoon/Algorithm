# 선택 정렬(Selection sort, O(n^2))
# BOJ #2750

# Test code
# 5
# 5
# 2
# 3
# 4
# 1

lst = []
smallest = 0
n = int(input())
for _ in range(n):
    x = int(input())
    lst.append(x)

for i in range(n-1):
    smallest = i
    for j in range(i+1, n):
        if lst[smallest] > lst[j]:
            smallest = j
    lst[i], lst[smallest] = lst[smallest], lst[i]

for k in range(n):
    print(lst[k])