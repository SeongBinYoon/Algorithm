# 창문 닫기

n = int(input())

'''
# list로 접근 -> 메모리 초과
# 창문, 모두 닫혀 있음, 0=닫힘/1=열림
window = [0 for _ in range(n)]

# 1부터 돌아가며 배수번째 창문 반대로 수행
for j in range(1, n+1):                 # j=1~n
    for k in range(j, n+1, j):          # j부터 n까지 j만큼 뛰어가며
        # k-1번째가 0이면 1로 변환
        if window[k-1] == 0:
            window[k-1] = 1
        # k-1번째가 1이면 0으로 변환
        else:
            window[k-1] = 0
print(window.count(1))
'''

# 규칙 -> 매 제곱마다 +1씩 늘어남. 루트n의 값(소수점 절삭)이 답  
print(int(n**(1/2)))