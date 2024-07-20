# 11653 소인수분해

n = int(input())

# 2와 3으로 계속 나누어본다.
while True:
    if n % 2 == 0:
        n = n // 2
        print(2)
    elif n % 3 == 0:
        n = n // 3
        print(3)
    else:
        break
# 더 이상 나뉘지 않아 반복문을 빠져나오면, 다시 반복하며 1~n까지 수로 나눈 나머지가 0이 되는 수를 찾는다. -> 소수임.
i = 2
while n != 1:
    if n % i == 0:
        n = n // i
        print(i)
        i = 1
    i += 1