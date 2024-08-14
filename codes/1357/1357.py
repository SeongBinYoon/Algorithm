# 1357 뒤집힌 덧셈

x, y = map(int, input().split())
# Rev(X), Rev(Y)
new_x = 0
new_y = 0
# x, y의 길이
len_x = len(str(x))
len_y = len(str(y))
# x 뒤집기
for i in range(len_x):
    tool_x = 10**(len_x - i - 1)
    new_x += (x // tool_x) * (10**i)
    x = x % tool_x
# y 뒤집기
for j in range(len_y):
    tool_y = 10**(len_y - j - 1)
    new_y += (y // tool_y) * (10**j)
    y = y % tool_y

# Rev(X)+Rev(Y)
sumofrev = new_x + new_y
res = 0
len_res = len(str(sumofrev))
# Rev(Rev(X)+Rev(Y))
for k in range(len_res):
    tool_res = 10**(len_res - k - 1)
    res += (sumofrev // tool_res) * (10**k)
    sumofrev = sumofrev % tool_res
print(res)