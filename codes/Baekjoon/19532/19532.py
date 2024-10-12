# 19532 수학은 비대면강의입니다

'''
# 이렇게 풀면 모든 경우의 수를 찾기 어려움 -> 틀린 코드
a, b, c, d, e, f = map(int, input().split())
# b가 0인 경우
if b == 0:
    x = c/a
    y = (c-a*x)/b
# e가 0인 경우
elif e == 0:
    x = f/d
    y = (c-a*x)/b
# a가 0인 경우
elif a == 0:
    y = c/b
    x = (f-e*y)/d
# d가 0인 경우
elif d == 0:
    y = f/e
    x = (c-b*y)/a
# y의 계수가 같은 경우 (3, 3)
elif b == e:
    x = (c-f)/(a-d)
    y = (c-a*x)/b
# y의 계수가 더하면 0인 경우 (3, -3)
elif b + e == 0:
    x = (c+f)/(a+d)
    y = (c-a*x)/b
# y의 계수가 서로 다른 경우 (3, 1)
else:
    # b>e면 d에 b//e만큼 곱
    if b > e:
        d *= b/e
        f *= b/e
        x = (c-f)/(a-d)
        y = (c-a*x)/b
    # b<e면 a에 e//b만큼 곱
    else:
        a *= e/b
        c *= e/b
        x = (c-f)/(a-d)
        y = (c-a*x)/b
#y = (c-a*x)/b
print(int(x), int(y))
'''

# 브루트 포스는 연립 방정식이나 식이 주어졌을 때, 식을 있는 그대로 사용하는 것이 낫다.
# brute force
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x+b*y==c) and (d*x+e*y==f):
            print(x, y)