# 유한소수 판별하기

# 최대공약수 함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def solution(a, b):
    answer = 1
    target = gcd(a,b)
    # a,b를 각각 최대공약수로 나누어 만든 기약분수의 분모
    lower = b // target
    # 분모가 1이 될 때 종료
    while lower != 1:
        if lower % 2 == 0:
            lower = lower // 2
        elif lower % 5 == 0:
            lower = lower // 5
        # 2로도 5로도 나누어 떨어지지 않으면 답은 2
        else:
            answer = 2
            break
    # 정상적으로 종료되면 유한소수인 것
    return answer