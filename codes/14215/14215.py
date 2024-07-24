# 14215 세 막대

import sys
input = sys.stdin.readline
# 입력 받기
x, y, z = map(int, input().split())

# max값 = 기준 값
std = max(x, y, z)
# 나머지 값의 합
rest = x + y + z - std

# 세 막대 길이가 모두 같은 경우
if x == y == z:
    print(x + y + z)
# 세 막대 길이가 모두 같지 않은 경우
else:
    # 두 값의 합이 가장 큰 값보다 작은 경우 (ex.1 1 100)
    if rest <= std:
        print(rest + rest - 1)
    # 두 값의 합이 가장 큰 값보다 큰 경우 (ex.3 4 3)
    else:
        print(rest + std)