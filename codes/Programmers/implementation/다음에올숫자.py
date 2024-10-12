# 다음에 올 숫자

def solution(common):
    
    # 등차수열인 경우
    if (common[1] - common[0]) == (common[2] - common[1]):
        dif = common[1] - common[0]
        ans = common[-1] + dif
    else:
        dif = common[2] // common[1]
        ans = common[-1] * dif
    return ans