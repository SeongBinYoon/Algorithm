# 4470 줄번호

n = int(input())
lst = []
for _ in range(n):
    x = input()
    lst.append(x)

for i in range(n):
    lst[i] = f"{1+i}" + ". " + lst[i]

for j in range(n):
    print(lst[j])