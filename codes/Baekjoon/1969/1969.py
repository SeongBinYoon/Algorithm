# 1969 DNA

import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
dic = {}
lst = []

for _ in range(n):
    lst.append(input())
res = ''
cnt = 0
for i in range(m):
    for j in range(n):
        if lst[j][i] in dic.keys():
            dic[lst[j][i]] += 1
        else:
            dic[lst[j][i]] = 1
    # sort - value별 내림차순, key별 오름차순
    dic = dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
    # 첫번째 key만 추가, 첫번째 value 누적
    for k, v in dic.items():
        res += k
        cnt += v
        break
    dic.clear()
print(res)
# 전체 문자 개수에서 첫번째 value 누적 차=Hamming distance
print((n * m) - cnt)