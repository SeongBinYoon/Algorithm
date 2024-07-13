# 11023 더하기3

acc = 0
x = input().split()
for i in range(len(x)):
    acc += int(x[i])

print(acc)