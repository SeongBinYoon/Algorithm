# 1269 대칭 차집합

dic = {}
cnt = 0
n, m = map(int, input().split(' '))
nlst = list(map(int, input().split(' ')))
mlst = list(map(int, input().split(' ')))

# A 집합 딕셔너리 추가
for i in nlst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# B 집합 딕셔너리 추가
for j in mlst:
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1
# value값 1이면 카운트 + 1
for k, v in dic.items():
    if v == 1:
        cnt += 1
print(cnt)