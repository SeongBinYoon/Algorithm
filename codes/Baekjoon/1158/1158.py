# 1158 요세푸스 문제

from collections import deque

n, k = map(int, input().split(' '))
# 큐 선언
dq = deque([i for i in range(1, n+1)])
# 정답 리스트
answer = []
# 큐가 비워질 때까지 반복
while len(dq) != 0:
    dq.rotate(-(k-1))               # k-1만큼 회전, 양수면 오른쪽으로, 음수면 왼쪽으로
    answer.append(dq[0])            # 맨 앞 수 선택
    dq.popleft()                    # 맨 앞 수 제거

# 결과 출력
print('<', end='')
for j in range(len(answer)):
    # 마지막 수인 경우
    if j == len(answer) - 1:
        print(answer[j], end='')
        print('>')
    else:
        print(answer[j], end=', ')