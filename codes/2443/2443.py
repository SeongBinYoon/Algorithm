# 2443 별찍기-6

n = int(input())
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for k in range(2*n-1-2*i):
        print('*', end='')
    print()