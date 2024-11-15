# 1620 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

'''
# 시간초과 발생
def solution(dic, question):
    # 문제 하나씩 돌며
    for i in range(len(question)):
        # key, value값에서 알맞은 정답 출력
        for k, v in dic.items():
            if question[i] == v:
                print(k)
            elif question[i] == k:
                print(v)

dic = {}
question = []
cnt = 1
n, m = map(int, input().split(' '))
# 도감 n개 딕셔너리에 번호 별 추가
for _ in range(n):
    dic[str(cnt)] = input().rstrip()
    cnt += 1
# 문제 m개 리스트에 추가
for _ in range(m):
    question.append(input().rstrip())
solution(dic, question)
'''

dic = {}
cnt = 1
n, m = map(int, input().split(' '))

# 도감 dictionary에 숫자, 이름 모두 key로 추가
for _ in range(n):
    name = input().rstrip()
    dic[str(cnt)] = name
    dic[name] = str(cnt)
    cnt += 1

for _ in range(m):
    question = input().rstrip()
    print(dic[question])