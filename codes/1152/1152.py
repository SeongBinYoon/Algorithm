# 1152 단어의 개수
'''
arr = []
stc = input()
arr = stc.split(sep=" ")
wordset = set(arr)
if "" in wordset:
    wordset.remove("")
print(len(wordset))
'''

arr = []
idx = 0
word = ""
stc = input()
for s in stc:
    if s != " ":
        word += s
    else:
        arr[idx].append(word)
        idx += 1