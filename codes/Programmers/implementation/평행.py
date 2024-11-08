# 평행

def solution(dots):
    answer = 0
    line1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    line2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    line3 = (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0])
    line4 = (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0])
    line5 = (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0])
    line6 = (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
    if line1 == line2:
        answer = 1
    elif line3 == line4:
        answer = 1
    elif line5 == line6:
        answer = 1
    return answer