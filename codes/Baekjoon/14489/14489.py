# 14489 치킨 두 마리

a, b = map(int, input().split())
ch = int(input())

s = a + b
price = ch * 2
if s < price:
    print(s)
else:
    res = s - price
    print(res)