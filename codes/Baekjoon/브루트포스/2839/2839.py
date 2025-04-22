# 2839 설탕 배달

# brute force
# 5를 기준으로 빼나가는 것이 아닌
# 3을 계속 빼나가며 5로 나누어 떨어지는지 확인한다
# 어차피 기준 삼아야 하는 가장 큰 봉지는 5kg이므로
n = int(input())

# 봉지 개수
cnt = 0

# n = 0이 되면 if 조건으로 들어가 n = 0인 채로 break됨
while n >= 0:
    # 5로 나누어 떨어지면 break
    if n % 5 == 0:
        cnt += int(n // 5)
        n = n % 5
        break
    n -= 3
    cnt += 1

# n이 음수 = 3kg과 5kg으로 정확히 nkg을 만들 수 없다
if n < 0:
    print(-1)
else:
    print(cnt)


# 잘못 생각한 코드 -> 5를 기준으로 빼나가지 말고 반대로 생각하자
'''
n = int(input())

# 5, 3kg 봉지
cnt_five = 0
cnt_three = 0

# 남은게 2이하면 종료
while n >= 5:
    # 5로 나누어떨어지면 몫이 정답이 되어 break
    if n % 5 == 0:
        cnt_five = n // 5
        n = n % 5
        break
    # 5kg 하나 할당
    n = n - 5
    cnt_five += 1
# 남은게 0이면 정답 출력 -> 0은 여기서 걸러짐
if n == 0:
    # 정답 출력
    print(cnt_five + cnt_three)
# 남은게 3이면 여기서 걸러짐
elif n == 3:
    print(1)
# 남은게 1,2,4면 -1 출력 -> 1,2,4는 여기서 걸러짐
else:
    print(-1)
'''