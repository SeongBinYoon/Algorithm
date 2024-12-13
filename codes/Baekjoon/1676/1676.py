# 1676 팩토리얼 0의 개수

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def zeroprint(k):
    cnt = 0
    target = str(k)
    for _ in range(len(target)):
        if target[-1] != '0':
            break
        cnt += 1
        target = target[:-1]

    return cnt

n = int(input())
k = factorial(n)
print(zeroprint(k))