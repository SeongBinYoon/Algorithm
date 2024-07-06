# 5622 다이얼
# 딕셔너리 가능

acc = 0
num = ""
s = input()
while s != "":
    if s[0] in ('A', 'B', 'C'):
        num += '2'
    elif s[0] in ('D', 'E', 'F'):
        num += '3'
    elif s[0] in ('G', 'H', 'I'):
        num += '4'
    elif s[0] in ('J', 'K', 'L'):
        num += '5'
    elif s[0] in ('M', 'N', 'O'):
        num += '6'
    elif s[0] in ('P', 'Q', 'R', 'S'):
        num += '7'
    elif s[0] in ('T', 'U', 'V'):
        num += '8'
    else:
        num += '9'
    s = s[1:]

for n in num:
    acc += int(n) + 1
print(acc)