# 7785 회사에 있는 사람

def solution(dic):
    answer = []
    for k, v in dic.items():
        if v == "enter":
            answer.append(k)
    answer.sort(reverse=True)
    for s in answer:
        print(s)

dic = {}
n = int(input())
for _ in range(n):
    name, condition = map(str, input().split(' '))
    dic[name] = condition
solution(dic)