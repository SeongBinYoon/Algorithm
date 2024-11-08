# 대문자와 소문자

def solution(my_string):
    answer = ''
    for s in my_string:
        if s.isupper():
            answer += s.replace(s, s.lower())
        else:
            answer += s.replace(s, s.upper())
    # for i in range(len(my_string)):
        # if my_string[i].isupper():
            # answer += my_string[i].replace(my_string[i], my_string[i].lower())
        # else:
            # answer += my_string[i].replace(my_string[i], my_string[i].upper())
    return answer