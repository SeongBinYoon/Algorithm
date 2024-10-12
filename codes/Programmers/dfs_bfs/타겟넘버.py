# 타겟 넘버

def solution(numbers, target):
    answer = 0
    # bfs
    lst = [0]
    for n in numbers:
        tmp = []
        for s in lst:
            tmp.append(s + n)
            tmp.append(s - n)
        lst = tmp
    for i in range(len(lst)):
        if lst[i] == target:
            answer += 1
    return answer