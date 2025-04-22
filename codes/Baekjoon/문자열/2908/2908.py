# 2908 상수

new_arr = []
num = ""
arr = input().split()
for s in arr:
    num += s[2] + s[1] + s[0]
    new_arr.append(num)
    num = ""

print(max(new_arr))