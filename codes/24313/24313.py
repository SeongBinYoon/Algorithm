# 24313 알고리즘 수업-점근적 표기1

def isbigo(a1, a0, c, n0):
    fn = a1 * n0 + a0
    gn = n0
    if fn <= c * gn and a1 <= c:
        return 1
    else:
        return 0

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
res = isbigo(a1, a0, c, n0)
print(res)