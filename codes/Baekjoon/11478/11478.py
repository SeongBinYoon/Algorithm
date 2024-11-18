# 11478 서로 다른 부분 문자열의 개수

# 부분 문자열 구하고 -> dictionary에 없으면 dictionary에 추가, 있으면 아무 것도 수행 x

s = input()
lst = []                            # 부분문자열 리스트
tmp = ''

# 부분 문자열 구하기
for i in range(len(s)):             # 5번, 0,1,2,3,4
    for j in range(len(s)-i):       # i=0일 때, j=0,1,2,3,4 / i=1일 때, j=0,1,2,3...
        tmp = s[j:i+j+1]            # [0:1], [1:2], [2:3], [3:4], [4:5] / [0:2], [1:3], [2:4], [3:5]
        lst.append(tmp)
# print(lst)

# 서로 다른 부분 문자열 구하기
dic = {}
for k in lst:
    # 부분 문자열이 dictionary에 있으면 value값 +1
    if k in dic:
        dic[k] += 1
    # 부분 문자열이 dictionary에 없으면 value값=1
    else:
        dic[k] = 1
# print(dic)

# dictionary의 key개수 출력
print(len(dic))