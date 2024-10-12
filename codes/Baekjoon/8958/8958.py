# 8958 OX퀴즈

n = int(input())
score = 0
acc = 0

for _ in range(n):
    x = input()
    for i in range(len(x)):
        if x[i] == 'X':
            score = 0
        else:
            score += 1
        acc += score
    print(acc)
    score = 0
    acc = 0