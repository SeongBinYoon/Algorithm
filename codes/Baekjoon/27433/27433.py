# 27433 팩토리얼2

# 팩토리얼 함수
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))