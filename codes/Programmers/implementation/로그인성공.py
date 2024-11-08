# 로그인 성공?

def solution(id_pw, db):
    answer = ''
    # db를 확인
    for i in range(len(db)):
        # id가 같은 경우
        if id_pw[0] == db[i][0]:
            # pw 일치하면 login
            if id_pw[1] == db[i][1]:
                answer = "login"
            # id는 같은데 pw가 일치하지 않으면 wrong pw
            else:
                answer = "wrong pw"
    # 모두 확인한 결과 answer가 ''면 fail
    if answer == '':
        answer = "fail"
    return answer