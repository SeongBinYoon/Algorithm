# 1181 단어 정렬
# 리스트 -> set -> 리스트 -> 비교, 정렬

def word_assign(word):
    word_set = set(word)
    new_word = list(word_set)
    n = len(new_word)
    '''
    # 길이대로 & 알파벳대로 버블 정렬 -> 시간 복잡도 높음
    for i in range(n-1):
        for j in range(n-i-1):
            if len(new_word[j]) > len(new_word[j+1]) or (new_word[j] > new_word[j+1] and len(new_word[j]) == len(new_word[j+1])):
                new_word[j], new_word[j+1] = new_word[j+1], new_word[j]
    # print(new_word)
    '''
    new_word.sort(key=lambda x: (len(x), x))
    
    for s in range(n):
        print(new_word[s])

word = []
N = int(input())
for _ in range(N):
    word.append(input())
word_assign(word)