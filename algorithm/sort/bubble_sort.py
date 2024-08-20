# 버블 정렬(Bubble sort, O(n^2))
# BOJ #2750

# Test code
# 5
# 5
# 2
# 3
# 4
# 1

lst = []
n = int(input())
for _ in range(n):
    lst.append(int(input()))

for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for j in range(len(lst)):
    print(lst[j])
