# 이진수 더하기

def solution(bin1, bin2):
    answer = ''
    answer = tentotwo(twototen(bin1) + twototen(bin2))
    return answer

# 2진수를 10진수로
def twototen(bin):
    res = 0
    # 문자열을 확인
    for i in range(len(bin)):
        # i번째 문자열이 1인 경우
        if bin[i] == '1':
            res += 2**(len(bin) - 1 - i)
    return res

# 10진수를 2진수로
def tentotwo(num):
    answer = ''
    # num이 마지막 1이 될 때까지
    while num > 1:
        # 나머지를 문자열에 추가
        answer = str(num % 2) + answer
        # num 변경
        num = num // 2
    answer = str(num) + answer
    return answer