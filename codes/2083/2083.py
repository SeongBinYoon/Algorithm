# 2083 럭비 클럽

reslst = []
while True:
    name, age, weight = input().split()
    age = int(age)
    weight = int(weight)
    if name == '#' and age == 0 and weight == 0:
        break
    if age > 17 or weight >= 80:
        reslst.append(name + ' Senior')
    else:
        reslst.append(name + ' Junior')
for i in range(len(reslst)):
    print(reslst[i])