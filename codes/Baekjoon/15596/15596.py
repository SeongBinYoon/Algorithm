# 15596 정수 N개의 합

def solve(a):
    acc = 0
    for i in range(len(a)):
        acc += a[i]
    return acc


a = []
while True:
    try:
        num = int(input())
        a.append(num)
    except EOFError:
        solve(a)
        break
