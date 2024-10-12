# 2475 검증수

n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])

acc = 0
for j in range(len(n)):
    acc += n[j]**2
res = acc % 10
print(res)