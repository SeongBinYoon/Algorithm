# 10814 나이순 정렬

def age_sort(lst):
    lst.sort(key=lambda x: x[0])
    for i in range(len(lst)):
        for j in range(2):
            print(lst[i][j], end=' ')
        print()    

lst = []
N = int(input())
for _ in range(N):
    age, name = map(str, input().split(' '))
    box = [int(age), name]
    lst.append(box)
age_sort(lst)