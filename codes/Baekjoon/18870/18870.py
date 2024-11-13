# 18870 좌표 압축

import sys
input = sys.stdin.readline

'''
# 시간복잡도 O(N^2) -> 시간초과
def solution(lst):
    cnt = 0
    answer = []
    # 복사
    tmp = lst.copy()
    # 중복 제거
    tmp = set(tmp)
    # lst를 하나씩 돌며 답을 구함
    for i in range(len(lst)):
        for j in tmp:
            if lst[i] > j:
                cnt += 1
        answer.append(cnt)
        cnt = 0
    for s in answer:
        print(s, end=' ')
    
    return 0
'''

'''
# list -> set으로 중복 제거 -> 다시 list로 -> sort -> index 번호 받기 -> 시간복잡도 O(N^2) -> 시간초과
# index 함수는 시간복잡도 O(N)으로, for문으로 N번 수행하므로 시간복잡도가 O(N^2)
def solution(lst):
    tmp = lst.copy()    # [2,4,-10,4,-9]
    tmp = set(tmp)      # (2,4,-10,-9)
    tmp = list(tmp)     # [2,4,-10,-9]
    tmp.sort()          # [-10,-9,2,4]
    for i in range(len(tmp)):
        print(tmp.index(lst[i]), end=' ')
'''

# list -> set -> list -> sort -> dictionary 저장 -> 성공
# dictionary의 시간복잡도는 O(1)로, for문으로 N번 수행하므로 시간복잡도가 O(N)
# index 함수보다 dictionary가 시간복잡도 작다.
def solution(lst):
    dic = {}
    idx = 0
    tmp = lst.copy()    # [2,4,-10,4,-9]
    tmp = set(tmp)      # (2,4,-10,-9)
    tmp = list(tmp)     # [2,4,-10,-9]
    tmp.sort()          # [-10,-9,2,4]
    # dictionary에 순서 저장
    for i in range(len(tmp)):
        dic[tmp[i]] = idx
        idx += 1
    # 결과 출력
    for j in range(len(lst)):
        print(dic[lst[j]], end=' ')

N = int(input())
lst = list(map(int, input().split(' ')))
solution(lst)