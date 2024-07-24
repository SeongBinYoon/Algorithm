# 10773 제로

n = int(input())
lst = []
res = 0
for _ in range(n):
    x = int(input())
    if x == 0:
        lst.pop()
    else:
        lst.append(x)
for i in range(len(lst)):
    res += lst[i]
print(res)