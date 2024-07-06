# 1152 단어의 개수
# -> 중복 단어 세어야 하므로 set은 x, 아래처럼 간단하게 구현 가능

arr = input().split()
print(len(arr))

'''
# 리스트 사용, 어렵게 구현한 것
arr = input().split(" ")
print(arr)
for s in arr:
    if s == "":
        idx = arr.index("")
        arr.pop(idx)
    print(arr)
print(len(arr))
'''

'''
# 중복 제외 시 set 이용 방법
stc = input().split(" ")
wordset = set(stc)
if "" in wordset:
    wordset.remove("")
print(len(wordset))
'''