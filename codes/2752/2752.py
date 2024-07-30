# 2752 세수정렬

lst = []
a, b, c = map(int, input().split())
lst.append(a)
lst.append(b)
lst.append(c)

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for k in range(len(lst)):
    print(lst[k], end=' ')