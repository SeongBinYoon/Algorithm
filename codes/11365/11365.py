# 11365 !밀비 급일

new_res = ''
while True:
    x = input()
    if x == "END":
        break
    for s in x:
        new_res = s + new_res
    print(new_res)
    new_res = ''