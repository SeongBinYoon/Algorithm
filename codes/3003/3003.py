# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰

ans = [1,1,2,2,2,8]
res = []
x = input().split()

for i in range(6):
    rest = ans[i] - int(x[i])
    res.append(rest)

for s in res:
    print(s, end=' ')