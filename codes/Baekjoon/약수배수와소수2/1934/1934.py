# 1934 최소공배수

# 최대공약수 함수
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split(' '))
    # 최대공약수
    target = gcd(a, b)
    x, y = a // target, b // target
    # 최소공배수 출력
    print(target * x * y)