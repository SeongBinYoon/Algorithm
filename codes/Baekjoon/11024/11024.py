# 11024 더하기4

acc = 0
lst = []
n = int(input())
for _ in range(n):
    x = input().split()

    for i in range(len(x)):
        acc += int(x[i])
    lst.append(acc)
    acc = 0

for j in range(len(lst)):
    print(lst[j])