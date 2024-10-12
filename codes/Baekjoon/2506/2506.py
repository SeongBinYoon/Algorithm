# 2506 점수계산

n = int(input())
lst = input().split()
acc = 0
res = 0

for i in range(n):
    lst[i] = int(lst[i])
    if lst[i] == 0:
        acc = 0
    else:
        acc += 1
        res += acc
print(res)