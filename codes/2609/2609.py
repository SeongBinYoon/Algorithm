# 2609 최대공약수와 최소공배수

'''
# 아래 코드는 유클리드 호제법(알고리즘)을 고려하지 않고 작성한 코드이다.
# 아래 코드는 2, 3만 고려하고 다른 소수는 고려하지 않아 147 343일 때, 1, 50421의 오류를 출력한다.
a, b = map(int, input().split())
# 최대공약수, 최소공배수
res1, res2 = 1, 1
large = max(a, b)
small = a + b - large
# 종료조건: (a==1 or b==1)
while (a != 1 and b != 1):
    large = max(a, b)
    small = a + b - large
    # 두 수 모두 2로 나누어 떨어지면
    if a % 2 == 0 and b % 2 == 0:
        # 2로 나눈 몫이 다음 a,b
        a, b = a // 2, b // 2
        # 최대공약수에 x2 누적
        res1 *= 2
    # 두 수 모두 3으로 나누어 떨어지면
    elif a % 3 == 0 and b % 3 == 0:
        # 3으로 나눈 몫이 다음 a,b
        a, b = a // 3, b // 3
        # 최대공약수에 x3 누적
        res1 *= 3
    # 2, 3 모두 나누어 떨어지지 않으면
    else:
        # 큰 수가 작은 수로 나누어 떨어지면
        if large % small == 0:
            a, b = small // small, large // small
            res1 *= small
        # 큰 수가 작은 수로 나누어 떨어지지 않으면
        else:
            break
res2 = res1 * a * b
print(res1)
print(res2)
'''

# 유클리드 호제법(알고리즘): 최대공약수를 구하는 방법
# gcd(m, n) = gcd(n, m mod n) (if n != 0) | m (if n == 0)
# 재귀이자 꼬리재귀임
# 최소공배수는 처음 m, n을 결과로 나온 최대공약수로 나눈 몫들과 최대공약수를 곱하면 됨
def gcd(m ,n):
    if n != 0:
        return gcd(n, m % n)
    else:
        return m

a, b = map(int, input().split())
# 최대공약수
res1 = gcd(a, b)
# 최소공배수
x, y = a // res1, b // res1
res2 = res1 * x * y
print(res1)
print(res2)