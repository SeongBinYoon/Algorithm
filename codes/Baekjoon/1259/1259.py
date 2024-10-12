# 1259 팰린드롬수

while True:
    n = input()
    # 마지막에 0 받으면 종료
    if n == '0':
        break
    # 한 자리 수인 경우는 모두 팰린드롬
    if len(n) == 1:
        print("yes")
    # 두 자리 수 이상인 경우
    else:
        for i in range(len(n)//2):
            # 다름이 발견되면 바로 break
            if n[i] != n[len(n)-i-1]:
                print("no")
                break
            # 같으면 계속 반복
            else:
                # 마지막 순번이면 yes 출력
                if i == (len(n)//2)-1:
                    print("yes")
                