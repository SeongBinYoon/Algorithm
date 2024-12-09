# 2346 풍선 터뜨리기
from collections import deque

n = int(input())
# balloon=풍선 번호, paper=종이에 쓰여진 수, answer=정답 리스트
balloon = deque([i for i in range(1, n+1)])
paper = deque(map(int, input().split(' ')))
answer = []
# print(balloon, paper)

# '앞 풍선 답 추가 -> 회전 -> 이전 풍선 제거' 순서는 불가능
# 덱에서 특정 인덱스 제거 불가 및 deque->list->deque 으로는 시간 복잡도와 효율성이 좋지 않음
# 따라서 '앞 풍선 답 추가 -> 앞 풍선 제거 -> 회전' 순서로 풀어야 함
# 앞 풍선은 제거되므로 회전 시 종이에 쓰인 수 그대로가 아닌 고려해주어야 함
for _ in range(n-1):
    # 제일 앞 풍선 번호
    target = balloon[0]
    # 제일 앞 풍선 종이에 쓰인 수
    idx = paper[0]
    # 제일 앞 풍선 일단 정답에 추가
    answer.append(target)
    # 제거 먼저
    balloon.popleft()
    paper.popleft()
    # rotate
    if idx > 0:
        balloon.rotate(-idx+1)
        paper.rotate(-idx+1)
    else:
        balloon.rotate(-idx)
        paper.rotate(-idx)
    # 터뜨린 풍선 제거
    # deque은 특정 인덱스의 요소를 제거할 수 없다.
    # 아래처럼 그냥 idx에 맞춰 remove한다면 paper의 중복된 요소의 경우 원하는 것을 삭제할 수 없다.
    # balloon.remove(balloon[-idx])
    # paper.remove(paper[-idx])
    # print(balloon, paper)
answer.append(balloon[0])

for s in answer:
    print(s, end=' ')