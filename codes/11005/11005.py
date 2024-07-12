# 11005 진법 변환2
# n을 b로 나눌 수 있을 때까지 나누고, 나머지를 아래에서 위로 읽는다.

# 알파벳 딕셔너리 정의
dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 
       19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R',
       28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}

n, b = map(int, input().split())
val = n # 0으로 초기화하면 반례 n=34, b=35가 잘못된 결과(0)로 출력됨
lst = []

# 몫이 b보다 작을 때까지 아래를 반복한다.
while n >= b:
    val = n // b # 몫
    res = n % b # 나머지
    n = val # 몫 최신화
    lst.append(res) # 빈 리스트에 나머지를 하나씩 저장
lst.append(val) # 더이상 나누어지지 않는 몫 저장
#print(lst)

# 채워진 리스트를 돌며 뒤에서부터 출력(딕셔너리에 있으면 해당 문자로 출력)
for i in range(len(lst)):
    value = lst[len(lst)-i-1]
    if value in dic:
       print(dic[value], end='')
    else:
       print(value, end='')