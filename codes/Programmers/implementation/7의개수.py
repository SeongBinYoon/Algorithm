# 7의 개수

def solution(array):
    answer = 0
    for i in range(len(array)):
        array[i] = str(array[i])
        for j in range(len(array[i])):
            if str(array[i][j]) == '7':
                answer += 1
    return answer