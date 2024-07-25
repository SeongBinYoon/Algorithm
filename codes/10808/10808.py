# 10808 알파벳 개수

# 알파벳
alpha = "abcdefghijklmnopqrstuvwxyz"
# 정답 리스트
res = [0 for _ in range(len(alpha))]

# 입력 받기
word = input()
# 받은 입력 문자 하나씩 돌며 카운팅
for x in word:
    idx = alpha.index(x)
    res[idx] += 1

# 출력
for i in range(len(res)):
    print(res[i], end=' ')