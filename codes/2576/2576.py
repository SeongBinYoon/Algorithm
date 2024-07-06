# 2576 홀수

arr = []
oddarr = []
acc = 0
count = 0
minval = 0

for _ in range(7):
    x = input()
    arr.append(int(x))

for num in arr:
    if num % 2 != 0:
        acc += num
        oddarr.append(num)

if len(oddarr) == 0:
    print(-1)
else:
    minval = min(oddarr)
    print(acc)
    print(minval)