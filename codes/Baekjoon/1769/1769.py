# 1769 3의 배수

x = input()
cnt = 0
# x가 한자리수가 될 때까지 반복
while len(x) != 1:
    tmp = 0
    for i in range(len(x)):
        tmp += int(x[i])
    x = str(tmp)
    cnt += 1
print(cnt)
# 3의 배수인지 확인
if int(x) % 3 == 0:
    print("YES")
else:
    print("NO")