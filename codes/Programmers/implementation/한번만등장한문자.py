# 한 번만 등장한 문자

def solution(s):
    answer = ''
    res = []
    for ch in s:
        if s.count(ch) == 1:
            res.append(ch)
    res.sort()
    for word in res:
        answer += word
    return answer