# 10809 알파벳 찾기

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
         "q","r","s","t","u","v","w","x","y","z"]
arr = []
for i in range(26):
    arr.append(-1)

word = input()
for i in range(len(word)):
    if word[i] in alpha:
        idx = alpha.index(word[i])
        if arr[idx] == -1:
            arr[idx] = i

for s in arr:
    print(s, end=" ")
