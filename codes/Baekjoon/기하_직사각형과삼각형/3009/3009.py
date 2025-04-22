# 3009 네 번째 점
import sys
input = sys.stdin.readline

xlst = []
ylst = []
xres = 0
yres = 0
for _ in range(3):
    x, y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)
    
for i in range(3):
    tmp1 = xlst.count(xlst[i])
    if tmp1 == 1:
        xres = xlst[i]
    tmp2 = ylst.count(ylst[i])
    if tmp2 == 1:
        yres = ylst[i]
print(xres, yres)
