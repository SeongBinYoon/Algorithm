# 9461 파도반 수열

import sys
input = sys.stdin.readline

# 메모
memo = [None for _ in range(101)]

# DP: Bottom-Up(Tabulation)
def padovan(n):
    # 기저
    memo[1], memo[2], memo[3], memo[4], memo[5] = 1, 1, 1, 2, 2
    
    # n=6부터 비어있으므로
    for i in range(6, n+1):
        memo[i] = memo[i-1] + memo[i-5]

    return memo[n]

# 입력
n = int(input())
for _ in range(n):
    print(padovan(int(input())))