# 치킨 쿠폰

# 반례: chicken = 1999
def solution(chicken):
    answer = service(chicken)
    return answer

def service(chicken):
    coupon = 0
    answer = 0
    # chicken이 10보다 작아질 때까지 반복
    while chicken >= 10:
        # 나머지는 쿠폰으로
        coupon += chicken % 10
        # 몫은 서비스 치킨 수로
        chicken = chicken // 10
        answer += chicken
    # 마지막 남은 것도 쿠폰으로
    coupon += chicken
    # 쿠폰 개수가 10개 이상이면 재귀호출
    if coupon >= 10:
        answer += service(coupon)
    return answer