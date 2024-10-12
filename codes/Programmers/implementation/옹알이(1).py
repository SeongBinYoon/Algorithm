# 옹알이(1)

def solution(babbling):
    answer = 0
    st = ["aya", "ye", "woo", "ma"]
    for i in range(len(st)):
        for j in range(len(babbling)):
            if st[i] in babbling[j]:
                idx = babbling[j].index(st[i])
                babbling[j] = babbling[j][:idx] + 'A' + babbling[j][idx+len(st[i]):]
    for k in range(len(babbling)):
        if babbling[k] == 'A' or babbling[k] == 'AA' or babbling[k] == 'AAA' or babbling[k] == 'AAAA':
            answer += 1
    return answer