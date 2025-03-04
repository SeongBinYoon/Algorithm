# Dynamic Programming(동적계획법)

# Bottom-Up(Tabulation)
# 아래에서부터 계산 수행, 누적시켜 전체 큰 문제 해결
# 반복문 사용

# Top-Down(Memoization)
# 위에서부터 바로 호출해 기저까지 내려간 후 재귀를 통해 결과를 재활용
# 재귀 사용

# 기존 재귀
def fibonacci(n):

    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# DP: Bottom-Up(Tabulation)
def fibonacci_bu(n):
    
    # 저장 리스트 초기화
    memo = [None] * 100
    memo[0], memo[1] = 0, 1

    # 반복문 사용
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


# DP: Top-Down(Memoization)
def fibonacci_td(n):
    
    # 저장 리스트 초기화
    memo = [None] * 100

    # 기저 도달
    if n <= 1:
        return n
    
    # n번째 피보나치 수가 저장되어 있지 않다면
    if memo[n] is None:
        memo[n] = fibonacci_td(n-1) + fibonacci_td(n-2)
    
    # n번째 피보나치 수가 저장되어 있다면
    return memo[n]


print(fibonacci(30))
print(fibonacci_bu(30))
print(fibonacci_td(30))