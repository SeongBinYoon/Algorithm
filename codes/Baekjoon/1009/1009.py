# 1009 분산처리
# 메모리 제한으로 인해 시간초과 -> 그냥 a**b가 아닌 규칙을 찾는다.
# 모든 한 자리 수 자연수 a는 4개씩 규칙이 있으므로 b / 4 후 나머지만큼 a에 제곱한다.

lst = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    pos = b % 4
    # b를 4로 나눈 나머지가 0이면 네제곱과 같음
    if pos == 0:
        pos = 4
    num = a ** pos
    com = num % 10
    # 0번 컴퓨터는 없음. 10번임.
    if com == 0:
        com = 10
    lst.append(com)

for i in range(len(lst)):
    print(lst[i])