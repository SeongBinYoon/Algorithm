# 1978 소수 찾기

# 입력 받기
n = int(input())
numlst = input().split()
# cnt=약수 개수, res=소수 개수
cnt, res = 0, 0
# n개 돈다.
for i in range(n):
    # 각 값
    num = int(numlst[i])
    # 각 값 % 1~값 (나머지) 개수가 2인지 확인
    for j in range(1, num+1):
        if num % j == 0:
            cnt += 1
    if cnt == 2:
        res += 1
    cnt = 0

print(res)