# 11399 ATM

n = int(input())
time = list(map(int, input().split(' ')))
acc = 0
time.sort()
for i in range(n):
    for j in range(i+1):
        acc += time[j]
print(acc)