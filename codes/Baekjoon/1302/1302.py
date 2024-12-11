# 1302 베스트셀러

dic = {}
n = int(input())
for _ in range(n):
    name = input()

    if name in dic.keys():
        dic[name] += 1
    else:
        dic[name] = 1

# value값에 대해 내림차순, key값에 대해 오름차순 정렬
dic = dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
# print(dic)
# 첫번째 key값만 출력
for k, v in dic.items():
    print(k)
    break