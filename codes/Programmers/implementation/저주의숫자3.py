# 저주의 숫자 3

def solution(n):
    answer = 0
    # 10진수
    ten = 1
    # 3x마을 수
    tx = 1
    # 10진수가 n+1과 같으면 종료
    while ten != (n+1):
        # tx가 3의 배수이거나 3이 들어있으면 조건에 해당하지 않을 때까지 +1
        if (tx % 3 == 0) or ('3' in str(tx)):
            while (tx % 3 == 0) or ('3' in str(tx)):
                tx += 1
        # tx가 3의 배수가 아니고, 3이 들어있지 않으면 다음 수로
        else:
            tx += 1
            # 10진수 +1
            ten += 1
    answer = tx - 1
    return answer