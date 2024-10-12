# 2440 별찍기-3

n = int(input())

for i in range(n):
    for j in range(n - i):
        print('*', end='')
    print()