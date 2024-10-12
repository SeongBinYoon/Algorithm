# 19944 뉴비의 기준은 뭘까?

n, m = map(int, input().split())
if m == 1 or m == 2:
    print("NEWBIE!")
elif 2 < m <= n:
    print("OLDBIE!")
else:
    print("TLE!")