# 2745 진법 변환

# 알파벳 딕셔너리 정의
dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 
       'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
       'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
# 누적값 변수
acc = 0
# 입력
x = input().split()
# B진법 수 N
num = x[0]
# B 값
jb = int(x[1])
# N을 돌아가며 
for i in range(len(num)):
    # B진법 수 N의 각 자리 요소들
    target = num[len(num) - i - 1]
    # 알파벳이 아닌 숫자일 경우
    if target.isdigit() == True:
        acc += int(target) * jb**i
    # 알파벳인 경우
    else:
        acc += dic[target] * jb**i
print(acc)