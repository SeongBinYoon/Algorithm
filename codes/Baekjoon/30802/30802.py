# 30802 웰컴 키트

n = int(input())
tshirts = list(map(int, input().split(' ')))
t, p =map(int, input().split(' '))
ans1, ans2, ans3 = 0, 0, 0
# 티셔츠
for s in tshirts:
    if s % t == 0:
        ans1 += (s // t)
    else:
        ans1 += (s // t) + 1
# 펜
ans2, ans3 = n // p, n % p
# 정답 출력
print(ans1)
print(ans2, ans3, sep=' ')