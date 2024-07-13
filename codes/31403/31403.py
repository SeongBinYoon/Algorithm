# 31403 A+B-C

lst = []
for _ in range(3):
    x = input()
    lst.append(x)

# 수로 생각했을 때
tmp = int(lst[0]) + int(lst[1])
res1 = tmp - int(lst[2])

# 문자열로 생각했을 때
tmp = lst[0] + lst[1]
res2 = int(tmp) - int(lst[2])

print(res1)
print(res2)