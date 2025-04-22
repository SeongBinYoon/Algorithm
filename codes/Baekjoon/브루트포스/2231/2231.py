# 2231 분해합

n = int(input())

lst = []
acc = 0

# 0~n 수 모두 조사
for i in range(n):
    num = str(i)
    # 수의 길이만큼 돌며 각 자리 수 합
    for j in range(len(num)):
        acc += int(num[j])
    # 각 자리 수 합과 값의 합
    acc += i
    # n과 같으면 생성자이므로 lst에 추가
    if acc == n:
        lst.append(i)
    acc = 0

# 생성자 없으면 0 출력
if len(lst) == 0:
    print(0)
else:
    print(min(lst))