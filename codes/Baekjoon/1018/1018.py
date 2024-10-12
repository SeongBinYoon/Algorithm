# 1018 체스판 다시 칠하기

# brute force: 8x8 크기만큼 다 돌기
n, m = map(int, input().split())
# 받아온 보드
board = []
# 결과 저장 리스트
res = []
# window 맨 좌상단이 각각 b, w일 때 고쳐야 하는 개수
acc_b = 0
acc_w = 0

# 행 별로 받아오기
for _ in range(n):
    x = input()
    board.append(x)
#print(board)

# 8x8크기만큼 돌며 확인
# 행은 n-7번 window sliding
for i in range(n-7):
    # 열은 m-7번 window sliding
    for j in range(m-7):
        # 8x8 window 내에서의 행
        for row in range(i, i+8):
            # 8x8 window 내에서의 열
            for col in range(j, j+8):
                # row+col이 짝수면 window 맨 좌상단과 같아야 함
                if (row + col) % 2 == 0:
                    # 짝수인데 B가 아니면
                    if board[row][col] != 'B':
                        # window 맨 좌상단이 b일 때 잘못 칠해진 것이므로 acc_b 증가
                        acc_b += 1
                    # 짝수인데 W가 아니면
                    else:
                        # window 맨 좌상단이 w일 때 잘못 칠해진 것이므로 acc_w 증가
                        acc_w += 1
                # row+col이 홀수면 window 맨 좌상단과 달라야 함
                else:
                    # 홀수인데 W가 아니면(B면)
                    if board[row][col] != 'W':
                        # window 맨 좌상단이 b일 때(같을 때) 잘못 칠해진 것이므로 acc_b 증가
                        acc_b += 1
                    # 홀수인데 B가 아니면(W면)
                    else:
                        # window 맨 좌상단이 w일 때(같을 때) 잘못 칠해진 것이므로 acc_w 증가
                        acc_w += 1
        # 8x8=64개 훑고 나면 세었던 acc를 리스트에 추가, 변수 초기화
        res.append(acc_w)
        res.append(acc_b)
        acc_w = 0
        acc_b = 0
print(min(res))


# 잘못된 코드-> window의 첫번째 부분을 정해두고 하는게 아닌, 모든 경우의 수를 따져야 한다.
# 특히, 체스문양은 row+col의 합의 짝/홀 여부로 알 수 있다.
'''
# 8x8크기만큼 돌며 확인
# 행은 n-7번 window sliding
for i in range(n-7):
    # 열은 m-7번 window sliding
    for j in range(m-7):
        # 8x8 window 내에서의 행
        for row in range(i, i+8):
            # 8x8 window 내에서의 열
            for col in range(j, j+8):
                # 맨 왼쪽 위 칸이 B인 경우
                if board[i][j] == 'B':
                    # 짝수 번째 행
                    if row % 2 == 0:
                        # 짝수 번째 열은 B여야
                        if col % 2 == 0:
                            if board[row][col] == 'W':
                                acc += 1
                        # 홀수 번째 열은 W여야
                        else:
                            if board[row][col] == 'B':
                                acc += 1
                    # 홀수 번째 행
                    else:
                        # 짝수 번째 열은 W여야
                        if col % 2 == 0:
                            if board[row][col] == 'B':
                                acc += 1
                        # 홀수 번째 열은 B여야
                        else:
                            if board[row][col] == 'W':
                                acc += 1
                # 맨 왼쪽 위 칸이 W인 경우
                elif board[i][j] == 'W':
                    # 짝수 번째 행
                    if row % 2 == 0:
                        # 짝수 번째 열은 W여야
                        if col % 2 == 0:
                            if board[row][col] == 'B':
                                acc += 1
                        # 홀수 번째 열은 B여야
                        else:
                            if board[row][col] == 'W':
                                acc += 1
                    # 홀수 번째 행
                    else:
                        # 짝수 번째 열은 B여야
                        if col % 2 == 0:
                            if board[row][col] == 'W':
                                acc += 1
                        # 홀수 번째 열은 W여야
                        else:
                            if board[row][col] == 'B':
                                acc += 1
        # 8x8=64개 훑고 나면 세었던 acc를 리스트에 추가, 변수 초기화
        res.append(acc)
        acc = 0
#print(cnt)
print(res)
'''