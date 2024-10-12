# 2476 주사위 게임

price = 0
target = 0
lst = []
n = int(input())
for _ in range(n):
    a, b, c = map(int,input().split())
    # 같은 눈이 3개
    if a == b == c:
        price = 10000 + a * 1000
        lst.append(price)
    # 모두 다른 눈
    elif a != b and b != c and a != c:
        target = max(a, b, c)
        price = target * 100
        lst.append(price)
    # 같은 눈이 2개
    else:
        if a == b:
            target = a
        elif b == c:
            target = b
        else:
            target = c
        price = 1000 + target * 100
        lst.append(price)
print(max(lst))

