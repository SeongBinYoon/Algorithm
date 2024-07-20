# 2581 소수

m = int(input())
n = int(input())
# cnt=약수 개수, psum=합, plst=소수리스트
cnt = 0
psum = 0
plst = []

# m이상 n이하 값 돈다.
for i in range(m, n+1):
    # 각 값에 대해 1~값까지 돈다.
    for j in range(1, i+1):
        # 나누어 떨어지면 cnt 증가
        if i % j == 0:
            cnt += 1
    # 소수면 합에 누적 + 리스트에 추가
    if cnt == 2:
        psum += i
        plst.append(i)
    cnt = 0

# 소수가 없을 경우 -1 출력
if psum == 0:
    print(-1)
else:
    # 합, 최솟값 출력
    print(psum)
    print(min(plst))