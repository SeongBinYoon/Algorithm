# 25192 인사성 밝은 곰곰이

import sys
input = sys.stdin.readline

# 인사한 사람을 담을 set
hello = set()
cnt = 0
n = int(input())
for _ in range(n):
    k = input().strip('\n')
    # ENTER면 set의 길이를 누적 + set 초기화
    if k == "ENTER":
        cnt += len(hello)
        hello.clear()
    # 그 외에는 set에 추가
    else:
        hello.add(k)
# 입력 종료 후 길이 누적
cnt += len(hello)
print(cnt)