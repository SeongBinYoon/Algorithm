# 2587 대표값2

lst = []
acc = 0
for _ in range(5):
    x = int(input())
    lst.append(x)
    acc += x

# 평균
avg = acc // 5
print(avg)

# 리스트 정렬
lst.sort()

# 중앙값
med = lst[len(lst) // 2]
print(med)