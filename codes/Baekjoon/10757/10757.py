# 10757 큰 수 A+B

# 작은 수 찾아 큰 수의 크기에 맞추어 앞에 '0' 추가 (123 9인 경우, 123 009)
a, b = map(int, input().split())
small = str(min(a, b))
big = str(max(a, b))
for _ in range(len(big) - len(small)):
    small = '0' + small

# 반복적으로 일의 자리 수 덧셈
ten = 0
one = 0
revres = ""
while small != "":
    x = str(int(small[-1]) + int(big[-1]) + ten)
    # 1을 넘겨줘야 할 때
    if len(x) == 2:
        ten = int(x[0])
        one = int(x[1])
    # 1을 넘겨주지 않을 때
    else:
        ten = 0
        one = int(x[0])
    revres = str(one) + revres
    small, big = small[:-1], big[:-1]
# 마지막에 1이 넘어가는 경우 (ex. 100 + 900)
if ten == 1:
    revres = str(ten) + revres

print(revres)