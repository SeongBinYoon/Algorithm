# 2675 문자열 반복

num = []
word = []
res = ""

n = input()
n = int(n)
for i in range(n):
    # 입력
    line = input()
    sp = line.split(sep=" ")
    # 반복 횟수 R
    num.append(int(sp[0]))
    # 문자열 S
    word.append(sp[1])

# 테스트 케이스 개수만큼 반복
for j in range(n):
    # word에 저장된 단어 하나씩
    for k in range(len(word[j])):
        # num에 저장된 반복 횟수만큼 반복해 변수에 이어 붙임
        for l in range(num[j]):
            res += word[j][k]
    print(res)
    # 테스트 케이스 끝날 때마다 변수 초기화
    res = ""