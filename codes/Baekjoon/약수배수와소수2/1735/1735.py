# 1735 분수 합
# 2 7
# 3 5

# 최대공약수(greatest common divisor) 함수
def gcd(m, n):
    if n == 0:
        return m
    else: 
        return gcd(n, m % n)

# 각 분자, 분모 입력
a1, b1 = map(int, input().split(' '))
a2, b2 = map(int, input().split(' '))

# 최소공배수(least common multiple, 합의 분모)
target1 = gcd(b1, b2)
x, y = b1 // target1, b2 // target1
lcm = target1 * x * y

# 분자에 곱해질 수 t1, t2
t1, t2 = y, x
# 분자의 합
upper = a1 * t1 + a2 * t2

# 기약분수 만들기
target2 = gcd(upper, lcm)
up = upper // target2
down = lcm // target2
print(up, down)