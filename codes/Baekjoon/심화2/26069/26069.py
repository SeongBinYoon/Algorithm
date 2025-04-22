# 26069 붙임성 좋은 총총이

dance = set()
n = int(input())
for _ in range(n):
    a, b = map(str, input().split(' '))
    if a == 'ChongChong':
        dance.add(b)
    elif b == 'ChongChong':
        dance.add(a)
    else:
        if a in dance:
            dance.add(b)
        elif b in dance:
            dance.add(a)
print(len(dance)+1)