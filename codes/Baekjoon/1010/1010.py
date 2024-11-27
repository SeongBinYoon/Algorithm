# 1010 다리 놓기

# 팩토리얼 재귀 함수
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' '))
    # mCn=m!/(m-n)!*n! 이므로
    tmp = m - n
    print(factorial(m) // (factorial(tmp) * factorial(n)))