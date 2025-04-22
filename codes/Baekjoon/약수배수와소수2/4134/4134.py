# 4134 다음 소수

import sys
input = sys.stdin.readline

'''
# 소수 판별 함수 (brute force 알고리즘) -> 시간초과
def isprime(n):
    while True:
        # 다음 수
        n += 1
        # cnt 초기화
        cnt = 0
        # i=1~n까지 돌며 해당 수가 나누어 떨어지면 cnt에 +1
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
        # 약수 개수가 1과 자기자신 즉, 2개면 소수이므로 break
        if cnt == 2:
            break
        cnt = 0
    return n
'''

'''
# 에라토스테네스의 체 알고리즘 -> indexerror
# indexerror -> n=1, 수가 0일 때 오류, 수가 1일 때 1, 수가 2일 때 2, 수가 3일 때 3으로 출력됨.
# 수가 4일 때 비로소 5가 됨.
def isprime(n):
    if n == 0 or n == 1:
        return 2
    elif n == 4:
        return 3
    elif n == 9:
        return 5
    # arr = [0,1,2,3,0,5,0,7,0,0,0,11,0,13,0,0,0]
    arr = [i for i in range(n+1)]
    # print(arr)
    end = int(n**(1/2))                 # end=4
    # arr[1] = 0                          # 1 또한 소수가 아니므로 제거
    for i in range(2, end+1):           # 2 ~ 4
        if arr[i] == 0:                 # 0이면(소수가 아닌 걸로 판정) 돌아가서 다음 수 확인
            continue
        for j in range(i*i, n+1, i):    # j=2일 때, 4,6,8,10...16, 2만큼 건너뜀/j=3일 때, 9,12,15, 3만큼 건너뜀
            arr[j] = 0
    # 0이 아니면 루트n번째(중심)부터 뒤 절반을 리스트로
    # tmp = [i for i in arr[int(n**(1/2)):] if arr[i]]
    # print(tmp)
    # return tmp[0]

    for s in arr[int(n**(1/2)):]:
        if s != 0:
            answer = s
            break
    return answer

n = int(input())
for _ in range(n):
    k = int(input())
    print(isprime(k**2))
'''

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
def position(k):
    # 0과 1의 다음 소수는 무조건 2
    if k == 0 or k == 1:
        return 2
    while True:
        # 소수면 그 값을 리턴
        if isprime(k):
            return k
        # 소수가 아니면 다음 수로 옮기고 그 수에 대해 다시 판별
        else:
            k += 1
            isprime(k)

n = int(input())
for _ in range(n):
    k = int(input())
    print(position(k))