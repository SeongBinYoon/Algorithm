# 삼각형의 완성조건(1)

def solution(sides):
    answer = 0
    max_side = max(sides)
    total_side = sides[0] + sides[1] + sides[2]
    if (total_side - max_side) > max_side:
        answer = 1
    else:
        answer = 2
    return answer