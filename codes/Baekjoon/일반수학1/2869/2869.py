# 2869 달팽이는 올라가고 싶다

# 반복문은 사용할 수 없다. 입력 크기가 천만 단위라 반복문을 사용할 경우 시간 초과 발생한다.
# v인 나무를 낮에 a 올라가고 밤에 b 내려간다. 맨 마지막에는 낮에 넘어간 a가 v보다 크면 그걸로 끝.
# 그렇다면 (전체 길이 - a)인 나머지 길이를 (a - b)로 나누면 경과일 수가 된다.

import sys
input = sys.stdin.readline
# a=올라가는 길이, b=내려가는 길이, v=전체 나무 길이
a, b, v = map(int, input().split())
day = 0
# a > v인 경우 ('='포함 안됨)
if a > v:
    print(1)
# a < v인 경우
else:
    # 나누어 떨어지는 경우 (ex.2 1 5 -> 3/1이 나누어 떨어진다.)
    if (v-a) % (a-b) == 0:
        day = (v-a) // (a-b) + 1
    # 나누어 떨어지지 않는 경우 (ex.5 1 6 -> 1/4가 나누어 떨어지지 않는다.)
    # 이런 경우 한 번 더 갈 수 있으므로 +2를 해준다.
    else:
        day = (v-a) // (a-b) + 2
print(day)

'''
# a=올라가는 길이, b=내려가는 길이, v=전체 나무 길이
a, b, v = map(int, input().split())
# 현재 위치한 층
floor = 0
# 올라간 층
top = 0
# 경과일 수
day = 0
while True:
    top = floor + a
    floor = top - b
    day += 1
    if top >= v:
        break
print(day)
'''