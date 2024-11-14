# 10815 숫자 카드

# 리스트에서 in은 for문과 동일한 시간복잡도 O(N)을 가진다. 따라서 이 방법은 O(N^2)의 시간복잡도를 가진다.
# set이나 dictionary에서 in은 O(1)이므로 보유 카드를 set에 넣고, 제시된 카드는 리스트로 처리한다.
def solution(cards, lst):
    for s in lst:
        if s in cards:
            print(1, end=' ')
        else:
            print(0, end=' ')

N = int(input())
cards = set(map(int, input().split(' ')))
M = int(input())
lst = list(map(int, input().split(' ')))
solution(cards, lst)