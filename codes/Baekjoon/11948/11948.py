# 11948 과목선택

lst1 = []
lst2 = []
for _ in range(4):
    grade = int(input())
    lst1.append(grade)
for _ in range(2):
    grade = int(input())
    lst2.append(grade)

lst1.sort()
lst2.sort()
res = lst1[-1] + lst1[-2] + lst1[-3] + lst2[-1]
print(res)