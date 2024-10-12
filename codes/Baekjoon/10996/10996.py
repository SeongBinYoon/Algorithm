# 10996 별찍기-21

n = input()
n = int(n)

# 한 세트를 n번 돎
for _ in range(n):
    # 한 세트 당 2번 돎
    for i in range(2):
        # 한 세트의 첫째 줄(별부터)
        if i == 0:
            # 한 줄에서 각 문자는 n번 출력
            for j in range(n):
                # i가 0,2,4,6이면 별 출력
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
        # 한 세트의 둘째 줄(공백부터)
        else:
            for j in range(n):
                # i가 0,2,4,6이면 공백 출력
                if j % 2 == 0:
                    print(' ', end='')
                else:
                    print('*', end='')
        print()