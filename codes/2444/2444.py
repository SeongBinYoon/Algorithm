# 2444 별찍기-7

n = input() # 5
n = int(n)

for i in range(n): # 5번
    for j in range(n - 1 - i): # 4, 3, 2, 1, 0
        print(' ', end='')
    for k in range(2 * i + 1): # 1, 3, 5, 7, 9
        print('*', end='')
    print()
for l in range((2 * n - 1)//2): # 4번
    for m in range(l + 1): # 1, 2, 3, 4
        print(' ', end='')
    for s in range(2*n-2*l-3): # 7, 5, 3, 1
        print('*', end='')
    print()