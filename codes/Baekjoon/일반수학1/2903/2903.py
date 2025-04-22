# 2903 중앙 이동 알고리즘
# 2^2, 3^2, 5^2, 9^2, 17^2, 33^2 순으로 늘어난다.

n = int(input())
cnt = 0
acc = 2
while n != 0:
    acc += 2**cnt
    res = acc**2
    cnt += 1
    n -= 1
print(res)