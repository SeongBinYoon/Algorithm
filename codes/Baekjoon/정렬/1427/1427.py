# 1427 소트인사이드

lst = []
n = input()
for r in n:
    r = int(r)
    lst.append(r)

# 버블 정렬 (bubble sort)
for i in range(len(lst)-1):
    for j in range(len(lst) - i - 1):
        if lst[j] < lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for k in range(len(lst)):
    print(lst[k], end='')