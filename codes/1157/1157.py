# 1157 단어 공부

def freqalphabet(word):
    dic = {}
    word = word.lower()
    for s in word:
        if s in dic.keys():
            dic[s] += 1
        else:
            dic[s] = 1
    #print(dic)
    # 리스트 컴프리헨션을 사용해 최대 value가 2개 이상일 때 key값을 찾는게 낫다.
    maxkey = [k for k, v in dic.items() if max(dic.values()) == v]
    if len(maxkey) != 1:
        res = '?'
    else:
        res = maxkey[0].upper()
    return res

x = input()
result = freqalphabet(x)
print(result)