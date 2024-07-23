# 5073 삼각형과 세 변

import sys
input = sys.stdin.readline

while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    # 가장 긴 변을 제외한 나머지 두 변의 합
    othsum = x + y + z - max(x, y, z)
    if max(x, y, z) >= othsum:
        print("Invalid")
    else:
        if x == y == z:
            print("Equilateral")
        elif x == y or y == z or x == z:
            print("Isosceles")
        else:
            print("Scalene")