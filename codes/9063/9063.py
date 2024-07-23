# 9063 대지

n = int(input())
xlst = []
ylst = []
for i in range(n):
    x, y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)
w = max(xlst) - min(xlst)
h = max(ylst) - min(ylst)
print(w * h)