# 2798 블랙잭

# brute force algorithm
n, m = map(int, input().split())
deck = input().split()
lst = []

# deck의 요소 int로 변환
for i in range(n):
    deck[i] = int(deck[i])

# 3장 골라서 m보다 작으면 더해서 lst 추가
# 첫번째 수
for i in range(n-2): # 0
    # 두번째 수
    for j in range(i+1, n-1): # 1 | 2
        # 세번째 수
        for k in range(j+1, n): # 2,3,4 | 3,4
            sumofdeck = deck[i] + deck[j] + deck[k]
            if m >= sumofdeck:
                lst.append(sumofdeck)
print(max(lst))