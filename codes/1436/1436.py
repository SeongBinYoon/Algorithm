# 1436 영화감독 숌

# brute force로 접근 -> 수를 그냥 1부터 센다
n = int(input())
# 번째 수
cnt = 0
# 값
val = 0

while True:
    # 값에 666이 포함되어 있다면 카운팅
    if '666' in str(val):
        cnt += 1
    # 카운팅이 n과 같으면 반복문 탈출
    if cnt == n:
        break
    # 값 1씩 증가 -> 모든 경우를 다 훑는다
    val += 1
print(val)


# 잘못된 코드 -> 너무 복잡하게 생각해 어디선가 잘못되었다
'''
# n = 번째
n = int(input())
# 초기 번째
i = 1
# 카운팅 수
cnt = 1
# 초기 영화제목
val = 666
tmp = 0
# i=n이면 종료
while i != n:
    # '5666'이 있으면 6666만들고 -6 후 끝자리 9될 때까지 1씩 증가
    if '5666' in str(val)[-4:]:
        # '6'+'666'=6666
        val = int(str(cnt) + '666')
        # 6666-6=6660
        val -= 6
        
        # 번째 수 i와 n이 같으면 종료, 마지막 자리수가 9면 종료
        while str(val)[-1] != '9':
            if i == n:
                #cnt += 1
                break
            if '6666' in str(val) or '66666' in str(val):
                cnt += 1
                i += 1
                val = int(str(cnt) + '666')
                break
            else:
                val += 1
                i += 1
        # 종료 후 마지막 자리 수가 9면 cnt 재개
        if str(val)[-1] == '9':
            cnt += 1
            
        print(val)
    # 처음 6666이 아니거나 일반적인 상황은 val 앞에 하나씩 카운트
    else:
        # 1+666
        val = int(str(cnt) + '666')
        cnt += 1
        # i 증가
        i += 1
        print(val)

print(val)
'''