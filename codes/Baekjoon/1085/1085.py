# 1085 직사각형에서 탈출
import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
res = min(abs(w-x), abs(h-y), x, y)
print(res)