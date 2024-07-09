# 25206 너의 평점은

acc = 0
total = 0
dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for i in range(20):
    x = input().split()
    if x[2] == 'P':
        pass
    else:
        acc += dic[x[2]] * float(x[1])
        total += float(x[1])
result = acc / total
print(round(result, 6))