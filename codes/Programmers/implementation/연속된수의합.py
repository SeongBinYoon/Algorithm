# 연속된 수의 합

'''
def solution(num, total):
    ans = []
    acc = 0
    # total-num+1번 완전탐색
    for i in range(total - num + 1):
        # num번 더함
        for j in range(num):
            acc += (i+1+j)
        # 확인    
        if acc == total:
            for k in range(num):
                i += 1
                ans.append(i)
            break
        acc = 0
    return ans
'''

def solution(num, total):
    ans = []
    # 나누어 떨어지면
    if total % num == 0:
        center = total // num
        for i in range(center-((num-1)//2), center+((num-1)//2)+1, 1):
            ans.append(i)
    else:
        standard = total // num # 3
        target = total % num # 2
        for j in range(standard-target+1, standard+target+1, 1):
            ans.append(j)
    return ans