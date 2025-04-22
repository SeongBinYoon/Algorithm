# 17103 골드바흐 파티션

import sys
input = sys.stdin.readline

# 에라토스테네스의 체
def sieve(n):
    # n=6일 때, [0,1,2,3,4,5,6], 이하 기본 frame 동일
    lst = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if lst[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            lst[j] = 0
    # 시간 복잡도를 조금이라도 줄이기 위해 list가 아닌 set으로 담는다.
    # 이 때, 슬라이싱이 아닌 범위로 준다.
    return {i for i in range(2, n+1) if lst[i]}

new_set = sieve(1000000)
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    # 2~(n//2)+1까지만 돌며(1은 소수 아니므로) 소수가 있다면 n에서 뺀 수도 소수인지만 확인
    # list의 탐색(in) = O(n), set의 탐색(in) = O(1)
    for i in range(2, n//2+1):
        if i in new_set and n-i in new_set:
            cnt += 1
    print(cnt)

'''
# 시간 초과 -> 이 방법의 시간복잡도는 O(t*n*루트n)이다.
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

# 골드바흐 파티션 함수
def gp(n):
    # <골드바흐 파티션>
    # 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
    # 1~(n//2)까지만 돌며 소수가 있다면 n에서 뺀 수도 소수인지만 확인
    m = 1
    k = n//2
    cnt = 0
    while True:
        # 종료 조건
        if m > k:
            break
        # m이 1인 경우 예외 처리
        if m == 1:
            m += 1
        # 소수면 n-k값도 소수인지 확인
        if isprime(m):
            if isprime(n-m):
                cnt += 1
        # 다음 수로
        m += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    print(gp(n))
'''