# A로 B만들기

def solution(before, after):
    answer = 0
    # before ''될 때까지 반복
    while before != '':
        # before 맨 앞 문자가 after에 있을 경우
        if before[0] in after:
            # after의 어느 위치에 있는지 확인
            idx = after.index(before[0])
            # 해당 부분 슬라이스 제거
            after = after[:idx] + after[idx+1:]
        before = before[1:]
    if after == '':
        answer = 1
    else:
        answer = 0
    return answer