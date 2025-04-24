# 1463 1로 만들기

n = int(input())

# 횟수를 담는 리스트
table = [0 for _ in range(1000001)]

# 리스트를 훑는다
for i in range(2, n+1):
    # i번째는 i-1번째 횟수의 +1
    table[i] = table[i-1] + 1
    # -1한 값과 2로 나눈 값의 횟수 중 더 최솟값을 선택
    if i % 2 == 0:
        table[i] = min(table[i], table[i//2] + 1)
    # -1한 값과 2로 나눈 값의 횟수 중 더 최솟값을 선택
    if i % 3 == 0:
        table[i] = min(table[i], table[i//3] + 1)
print(table[n])