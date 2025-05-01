# 10844 쉬운 계단 수

n = int(input())
# table[자릿수][맨 앞 숫자]
table = [[0 for _ in range(10)] for _ in range(n+1)]

# 한자릿수일 때
for s in range(1, 10):
    table[1][s] = 1

# 두자릿수부터
for i in range(2, n+1):
    for j in range(10):
        # 맨 앞 수가 0인 경우
        if j == 0:
            # 이전 자릿수의 1뿐임
            table[i][j] = table[i-1][1]
        # 맨 앞 수가 9인 경우
        elif j == 9:
            # 이전 자릿수의 8뿐임
            table[i][j] = table[i-1][8]
        # 맨 앞 수가 1~8인 경우
        else:
            # 이전 자릿수의 하나 전 숫자 + 이전 자릿수의 하나 다음 숫자
            table[i][j] = table[i-1][j-1] + table[i-1][j+1]

# print(table)
print(sum(table[n]) % 1000000000)