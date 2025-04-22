# 2580 스도쿠

import sys
input = sys.stdin.readline

# r=행 입력, board=스도쿠 보드 전체, blank=빈 칸의 [x, y] 좌표 리스트
r, board, blank = [], [], []

# 행 검사: x행의 열에 v가 있는지 검사
def check_row(x, v):
    for i in range(9):
        if board[x][i] == v:
            return False
    return True

# 열 검사: y열의 행에 v가 있는지 검사
def check_col(y, v):
    for j in range(9):
        if board[j][y] == v:
            return False
    return True

# 3x3 검사: x행, y열이 포함된 3x3 내에 v가 있는지 검사
def check_sq(x, y, v):
    # x행 y열이 포함된 3x3의 시작 좌표(7행 5열->6, 3)
    nx = x // 3 * 3
    ny = y // 3 * 3

    # 3x3을 돌며 확인
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j] == v:
                return False
    return True

# dfs + backtracking
def sudoku(n):
    
    # 종료 조건 (blank 모두 돈 경우)
    if n == len(blank):
        # 2중 리스트의 요소를 공백 기준 출력
        for _ in range(9):
            print(*board[_])
        exit(0)
    
    # 빈 칸의 x좌표
    x = blank[n][0]
    # 빈 칸의 y좌표
    y = blank[n][1]

    # 1~9까지 하나씩 넣으며 되는지 확인
    for v in range(1, 10):
        # 모두 가능할 때
        if check_row(x, v) and check_col(y, v) and check_sq(x, y, v):
            # 빈 칸의 좌표에 v값 적용
            board[x][y] = v
            # 다음 빈 칸 확인 위해 재귀 호출
            sudoku(n + 1)
            # for문을 다 돌아도 v값이 있으면 종료하고(다시 돌아오고) 바로 전 값 틀린 것임
            # 따라서 다시 0 적용
            board[x][y] = 0
    

# board 입력
for i in range(9):
    r = list(map(int, input().split()))
    board.append(r)
    # 빈 칸의 좌표 저장
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])

# 첫 호출(blank의 0번 인덱스)
sudoku(0)