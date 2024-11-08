# 369게임

def solution(order):
    answer = 0
    order = str(order)
    if '3' in order:
        order = order.replace('3', 'A')
    if '6' in order:
        order = order.replace('6', 'A')
    if '9' in order:
        order = order.replace('9', 'A')
    answer = order.count('A')
    return answer