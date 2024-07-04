# 2675 문자열 반복

num = []
word = []
res = ""

n = input()
n = int(n)
for i in range(n):
    line = input()
    sp = line.split(sep=" ")
    num.append(int(sp[0]))
    word.append(sp[1])

for j in range(n):
    for k in range(len(word[j])):
        for l in range(num[j]):
            res += word[j][k]
    print(res)
    res = ""