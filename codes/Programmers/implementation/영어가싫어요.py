# 영어가 싫어요

def solution(numbers):
    dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    # while numbers != '':
    for s in dic.keys():
        if s in numbers:
            numbers = numbers.replace(s, str(dic[s]))
    return int(numbers)