# 1251 단어 나누기

# brute force로 접근
k = list(input())
# 모든 str을 담을 리스트
answers = []
# # k=mobitel일 때, i=1~5
for i in range(1, len(k)-1):
    # j=2~6, 3~6, 4~6...
    for j in range(i+1, len(k)):
        a, b, c = reversed(k[:i]), reversed(k[i:j]), reversed(k[j:])
        answers.append(''.join(list(a)) + ''.join(list(b)) + ''.join(list(c)))
# 정렬 후 가장 앞 출력
print(sorted(answers)[0])

'''
# 아래 방법은 k에 중복 문자가 존재할 때 오류 발생
answer = ''
idx_first = k[:len(k)-2].index(min(k[:len(k)-2]))
idx_second = k[idx_first+1:-1].index(min(k[idx_first+1:-1]))
idx_second += idx_first+1
print(''.join(list(reversed(k[:idx_first+1])) + list(reversed(k[idx_first+1:idx_second+1])) + list(reversed(k[idx_second+1:]))))
'''