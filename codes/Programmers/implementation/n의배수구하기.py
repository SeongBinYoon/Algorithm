# n의 배수 구하기

def solution(n, numlist):
    answer = []
    while numlist != []:
        if numlist[0] % n == 0:
            answer.append(numlist[0])
        numlist = numlist[1:]
    return answer