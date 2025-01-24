# 4673 셀프 넘버

lst = [i for i in range(1, 10001)]

# 각 자릿수 더하는 함수
def acc(n):
    tmp = n
    while len(str(n)) != 1:
        n, b = n // 10, n % 10
        tmp += b
    return tmp + n

# j = 0
for j in range(len(lst)):
    # 생성자로 0이 된 경우는 다음 j(수)로 넘어감
    if lst[j] == 0:
        continue
    target = lst[j]
    # j가 정해지고 j부터 10000까지 생성자 있는 수 지우기
    while target < 10000:
        target = acc(target)
        if target <= 10000:
            lst[target-1] = 0

for i in range(10000):
    if lst[i]:
        print(lst[i])