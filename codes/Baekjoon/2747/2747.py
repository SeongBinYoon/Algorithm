# 2747 피보나치수
# 표채워풀기 알고리즘(while)

def fib(n):
    if n > 1:
        i = 2
        a, b = 0, 1 # a=fib(n-2), b=fib(n-1)
        while i <= n: # 2~n까지
            a, b = b, a + b
            i += 1
        return b
    else:
        return n

n = int(input())
res = fib(n)
print(res)