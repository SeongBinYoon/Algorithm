# 1764 듣보잡

dic = {}
answer = []
n, m = map(int, input().split(' '))
for _ in range(n+m):
    name = input()
    # dic에 있으면 1씩 증가
    if name in dic:
        dic[name] += 1
    # dic에 없으면 1
    else:
        dic[name] = 1

# value값이 2면 듣도 보도 못한 사람
for k, v in dic.items():
    if v == 2:
        answer.append(k)
answer.sort()
print(len(answer))
for s in answer:
    print(s)