# 2750 수 정렬하기

lst = []
n = int(input())
for _ in range(n):
    x = int(input())
    lst.append(x)
#print(lst)

new_lst = sorted(lst)
for k in range(n):
    print(new_lst[k])