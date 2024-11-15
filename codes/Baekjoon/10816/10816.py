# 10816 숫자 카드2

dic = {}
# 보유 카드 개수
n = int(input())
# 보유 카드 리스트
cards = list(map(int, input().split(' ')))
# 문제 개수
m = int(input())
# 문제 리스트
question = list(map(int, input().split(' ')))

# 딕셔너리에 보유 카드 정리
for i in range(n):
    # 딕셔너리에 보유 카드가 있으면
    if cards[i] in dic:
        dic[cards[i]] += 1
    # 딕셔너리에 보유 카드가 없으면
    else:
        dic[cards[i]] = 1

# 문제 리스트 돌며 value값 출력
for j in range(m):
    # 딕셔너리에 문제의 키 값이 있으면 value 출력
    if question[j] in dic:
        print(dic[question[j]], end=' ')
    # 딕셔너리에 문제의 키 값이 없으면 0 출력
    else:
        print(0, end=' ')