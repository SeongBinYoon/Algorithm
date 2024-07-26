# 11050 이항계수1

n, k = map(int, input().split())
acc = 1
div = 1
for i in range(k):
    acc *= n
    n = n - 1
for j in range(k):
    div *= k
    k = k - 1
res = acc // div
print(res)