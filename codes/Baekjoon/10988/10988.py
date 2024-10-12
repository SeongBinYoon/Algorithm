# 10988 팰린드롬인지 확인하기

def ispalindrome(word):
    res = 0
    leng = len(word)
    for i in range(leng):
        if word[i] == word[leng - 1 - i]:
            res = 1
        else:
            res = 0
            break
    return res

x = input()
answer = ispalindrome(x)
print(answer)