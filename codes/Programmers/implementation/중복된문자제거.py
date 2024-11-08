# 중복된 문자 제거

def solution(my_string):
    answer = ''
    # my_string 이 ''될 때까지 반복
    while my_string != '':
        # my_string의 첫번째 문자가 치환된 '0'인 경우
        if my_string[0] == '0':
            # 그냥 무시하고 당기고 while 루프 다시 돌아간다
            my_string = my_string[1:]
            continue
        # my_string의 첫번째 문자 개수가 2개 이상이면
        if my_string.count(my_string[0]) > 1:
            # 맨 앞 문자를 일단 answer에 추가
            answer += my_string[0]
            # 중복 문자들을 모두 숫자 '0'으로 치환
            my_string = my_string.replace(my_string[0], '0')
            
            # 문자 당기기
            my_string = my_string[1:]
        else:
            answer += my_string[0]
            my_string = my_string[1:]
        
    return answer