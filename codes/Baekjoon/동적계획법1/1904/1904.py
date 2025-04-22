# 1904 01타일

# 입력
n = int(input())

# 메모
memo = [None for _ in range(1000001)]

# DP: Bottom-Up(Tabulation)
def zero_one_tile(n):
    memo[0], memo[1], memo[2] = 1, 1, 2
    for i in range(3, n+1):
        memo[i] = (memo[i-1] + memo[i-2]) % 15746
    return memo[n]

'''
# DP: Top-Down(Memoization) -> recursion error 발생
def zero_one_tile(n):

    # 기저: 점화식 및 기저 피보나치와 동일
    if n < 3:
        return n
    # 메모되어 있지 않으면
    if memo[n] is None:
        memo[n] = (zero_one_tile(n-1) + zero_one_tile(n-2)) % 15746
    # 메모되어 있으면
    return memo[n]
'''

print(zero_one_tile(n))