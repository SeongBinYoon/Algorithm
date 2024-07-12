# 2720 세탁소 사장 동혁

lst = []
n = int(input())
for _ in range(n):
    x = int(input())
    val = x
    
    qcount = val // 25
    val = val % 25
    lst.append(qcount)
    dcount = val // 10
    val = val % 10
    lst.append(dcount)
    ncount = val // 5
    val = val % 5
    lst.append(ncount)
    pcount = val // 1
    val = val % 1
    lst.append(pcount)

for i in range(len(lst)):
    print(lst[i], end=' ')
    if (i + 1) % 4 == 0:
        print()