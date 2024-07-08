# 1316 그룹 단어 체커

def groupchecker(n):
    lst = []
    count = n
    for _ in range(n):
        word = input()
        lst.append(word)
    #print(lst)
    
    for i in range(n):
        for j in range(len(lst[i])-1):
            if lst[i][j] == lst[i][j+1]:
                pass
            elif lst[i][j] in lst[i][j+1:]:
                count -= 1
                break
    return count

n = int(input())
result = groupchecker(n)
print(result)

'''
x = input()
# list의 인덱스
loc = 0
list = []
cnt = 0
# True면 중복, False면 중복 없음
flag = False
# 받은 N만큼 반복
for i in range(x[0]):
    # 이전 리스트에
    for j in range(loc):
        # 같은 문자가 없으면 넣는다.
        if list[j] != x[i]:
            list.append(x[i+1])
            loc += 1
            
        # 같은 문자가 있으면 flag = True로 두고 
        else:
            flag = True
            continue
'''