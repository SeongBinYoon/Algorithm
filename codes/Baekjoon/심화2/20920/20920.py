# 20920 영단어 암기는 어려워

import sys
input = sys.stdin.readline

dic = {}
n, m = map(int, input().split(' '))
for _ in range(n):
    word = input().strip('\n')
    if len(word) >= m:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1

# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 해당 단어의 길이가 길수록 앞에 배치
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
dic = dict(sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0])))
for k, v in dic.items():
    print(k)