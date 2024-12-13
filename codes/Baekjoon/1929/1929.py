# 1929 소수 구하기

import sys
input = sys.stdin.readline

# 소수인지 아닌지 판별하는 함수
def isprime(n):
    # 2~int(루트n)+1까지 절반만 확인
    for i in range(2, int(n**(1/2))+1):
        # 도중에 나누어 떨어지면 소수가 아니므로 False 리턴
        if n % i == 0:
            return False
    # 끝까지 나누어 떨어지지 않았다면 소수이므로 True 리턴
    return True

# isprime 함수에 따라 소수면 바로 리턴, 소수가 아니면 다음 수로 옮기는 함수
def position(m, n):
    # m이 1인 경우 예외 처리
    while True:
        # 종료 조건
        if m > n:
            break
        # m이 1인 경우 예외 처리
        if m == 1:
            m += 1
        # 소수면 그 값을 리턴
        if isprime(m):
            print(m)
        # 다음 수로
        m += 1

m, n = map(int, input().split(' '))
position(m, n)