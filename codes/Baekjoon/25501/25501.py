# 25501 재귀의 귀재

import sys
input = sys.stdin.readline

# ABBA일 때, s=ABBA, l=0, r=3
def recursion(s, l, r, cnt):
    # position이 안쪽으로 움직이다가 같거나(단어길이 홀수) 넘기면(단어길이 짝수) 1 return
    if l >= r:
        print(1, end=' ')
        return cnt
    # s[0]과 s[3]이 다르면 팰린드롬이 아님
    elif s[l] != s[r]:
        print(0, end=' ')
        return cnt
    # position을 l은 오른쪽으로, r은 왼쪽으로 전체적으로 균형있게 안쪽으로 재귀호출
    else:
        return recursion(s, l+1, r-1, cnt+1)

# ABBA일 때, ABBA/0/3 전달
def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)

n = int(input())
for _ in range(n):
    word = input().strip('\n')
    # 재귀호출 카운트 변수
    cnt = 1
    print(isPalindrome(word, cnt))