# 13241 최소공배수

# 최대공약수 함수
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

a, b = map(int, input().split(' '))
target = gcd(a, b)
x, y = a // target, b // target
print(target * x * y)