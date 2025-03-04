# 24416 알고리즘 수업 - 피보나치 수 1

# 입력
n = int(input())
# 실행 횟수 변수
cnt1, cnt2 = 0, 0

# 재귀 사용
def fib(n):
    global cnt1

    if n == 1 or n == 2:
        # 코드1
        cnt1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

# DP(Tabulation) 사용
def fibonacci(n):
    global cnt2

    # memo, 초기 값
    f = [None] * 100
    f[1], f[2] = 1, 1

    # 3번째 값부터 반복하며 저장
    for i in range(3, n+1):
        # 코드2
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

# 출력
fib(n)
fibonacci(n)
print(cnt1, cnt2)