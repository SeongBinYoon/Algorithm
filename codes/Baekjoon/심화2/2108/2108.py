# 2108 통계학

import sys
input = sys.stdin.readline

lst = []
dic = {}
n = int(input())
for _ in range(n):
    k = int(input())
    lst.append(k)
    if k in dic.keys():
        dic[k] += 1
    else:
        dic[k] = 1

# 산술평균
acc = 0
for i in lst:
    acc += i
avg = acc / n
if avg < 0:
    if round(abs(avg), 0) == 0.0:
        print(0)
    else:
        print(int(-round(abs(avg), 0)))
else:
    print(int(round(avg, 0)))

# 중앙값
lst.sort()
print(lst[n//2])

# 최빈값
# value 내림차순, key 오름차순 정렬
dic = dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
# 여러 개 있을 시 두 번째로 작은 값 출력
tmp = -1
for k, v in dic.items():
    # 1번째와 2번째 value가 같으면
    if tmp == v:
        print(k)                    # 2번째 key 출력
        break                       # 반복문 종료
    # 1번째와 2번째 value가 다르고 tmp가 -1이 아니면
    elif tmp != v and tmp != -1: 
        print(firstkey)             # 1번째 key 출력
        break                       # 반복문 종료
    tmp = v
    firstkey = k
    if n == 1:
        print(firstkey)

# 범위
print(lst[-1] - lst[0])