# 2292 벌집
# 2~7까지(6개)는 2, 8~19까지(12개)는 3, 20~37까지(18개)는 4, 38~61까지(24개)는 5....와 같은 규칙을 가진다.

n = int(input())
if n == 1:
    print(n)
else:
    n = n - 2
    cnt = 1
    val = n // 6
    while val >= 0:
        val = val - cnt
        cnt += 1
    print(cnt)