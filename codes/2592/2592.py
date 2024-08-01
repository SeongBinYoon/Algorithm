# 2592 대표값

lst = []
freqlst = [0 for _ in range(100)]

for _ in range(10):
    n = int(input())
    lst.append(n)

total, avg = 0, 0
# 평균
for i in range(len(lst)):
    total += lst[i]
    freqlst[lst[i] // 10] += 1
avg = total // 10

# 최빈값
idx = freqlst.index(max(freqlst))
freq = idx * 10

print(avg)
print(freq)