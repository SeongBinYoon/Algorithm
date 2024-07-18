# 11721 열 개씩 끊어 출력하기

n = input()
res = ""
cnt = 0
while n != "":
    res += n[0]
    n = n[1:]
    cnt += 1
    if cnt == 10:
        cnt = 0
        res += '\n'
print(res)