# 10989 수 정렬하기3

# 메모리 초과 발생 -> 8MB 메모리 제한이 있는데 받는 수 개수는 10,000,000개까지 입력
# 따라서, 리스트나 sort, sorted 사용 x -> 계수정렬 활용
'''
lst = []
n = int(input())
for _ in range(n):
    x = int(input())
    lst.append(x)

for i in range(n-1):
    for j in range(i+1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for k in range(n):
    print(lst[k])
'''
'''
lst = []
n = int(input())
for _ in range(n):
    x = int(input())
    lst.append(x)
#print(lst)

new_lst = sorted(lst)
for k in range(n):
    print(new_lst[k])
'''

# stdin.readline을 사용해야 버퍼 사이즈 차이로 입력이 반복될수록 속도에서 우위를 가지므로 시간 초과가 발생하지 x
import sys
input = sys.stdin.readline

# 계수정렬
# 수의 크기는 10000까지이므로 크기 10000+1짜리 리스트를 선언
lst = [0 for _ in range(10001)]
n = int(input())

# 각 입력을 받아 해당하는 리스트 인덱스에 +1
for _ in range(n):
    x = int(input())
    lst[x] += 1

# 들어있는 값만큼 인덱스를 반복 출력
for i in range(len(lst)):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)