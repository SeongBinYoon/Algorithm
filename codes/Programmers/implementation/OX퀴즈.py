# OX퀴즈

def solution(quiz):
    answer = []
    for s in quiz:
        lst = []
        lst = s.split(' ')
        # -인 경우
        if lst[1] == '-':
            if (int(lst[0]) - int(lst[2])) == int(lst[4]):
                answer.append('O')
            else:
                answer.append('X')
        # +인 경우
        else:
            if (int(lst[0]) + int(lst[2])) == int(lst[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer