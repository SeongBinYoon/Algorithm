# 11720 숫자의 합

acc = 0
count = input()
count = int(count)
num = input()

for i in range(count):
    acc += int(num[i])

print(acc)