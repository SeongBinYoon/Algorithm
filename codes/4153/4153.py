# 4153 직각삼각형

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    else:
        longest = max(a, b, c)
        restsum = (a + b + c) -longest
        restmul = (a * b * c) // longest
        if (restsum**2 - 2 * restmul) == longest**2:
            print("right")
        else:
            print("wrong")