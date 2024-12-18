# 4948 베르트랑 공준

import sys
input = sys.stdin.readline

# 에라토스테네스의 체
def sieve(n):
    lst = [i for i in range(n+1)]
    end = int(n**(1/2))
    # 2~루트n까지만 확인, 대칭이므로 절반만 확인
    for i in range(2, end+1):
        # 소수가 아니면 다음 수로 건너 뜀
        if lst[i] == 0:
            continue
        # 약수가 있는 수(소수가 아닌) 제거
        for j in range(i*i, n+1, i):
            lst[j] = 0
    return lst

# 2배여야 범위를 넘어가도 계산됨
new_lst = sieve(123456*2)
while True:
    n = int(input())
    if n == 0:
        break
    # n보다 크고 2n보다 작거나 같은 수 중 소수
    ans = [i for i in new_lst[n+1:2*n+1] if new_lst[i]]
    print(len(ans))

'''
# 시간 초과 -> 이 방법의 시간복잡도는 O(n*루트n), 즉, n의 1.5제곱이다.
# 이보다 더 적은 에라토스테네스의 체(O(nloglogn))를 사용해야 한다.
# 소수인지 아닌지 판별하는 함수
def isprime(n):
    # 2~int(루트n)+1까지 절반만 확인
    for i in range(2, int(n**(1/2))+1):
        # 도중에 나누어 떨어지면 소수가 아니므로 False 리턴
        if n % i == 0:
            return False
    # 끝까지 나누어 떨어지지 않았다면 소수이므로 True 리턴
    return True

# isprime()에 따라 소수면 바로 리턴, 소수가 아니면 다음 수로 넘기는 함수
def position(m):
    # <베르트랑 공준>
    # 임의의 자연수 n에 대하여 n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재
    # 이에 맞춰 m과 n 설정
    n = m * 2
    m += 1
    cnt = 0
    while True:
        # 종료 조건
        if m > n:
            break
        # 소수면 그 값을 저장
        if isprime(m):
            cnt += 1
        # 다음 수로
        m += 1
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    print(position(n))
'''