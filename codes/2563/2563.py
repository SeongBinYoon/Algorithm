# 2563 색종이

# 좌표 평면을 오른쪽으로 90도 회전한 행렬이라고 생각한다.
# 각 지점에 크기 1짜리 정사각형이 있다고 생각한다.
# 리스트 컴프리헨션으로 이중 리스트를 만들고 0으로 채운다.
lst = [[0 for _ in range(100)] for _ in range(100)]
count = 0

# 색종이 개수 받기
n = int(input())

# 색종이 개수만큼 돌며 색종이에 해당하는 부분(x로부터 +10, y로부터 +10)을 1로 채운다.
# 예: 3행 7열부터 3행 8열, 9, 10, 11, 12, 13, 14, 15, 16, 17 / 4~13행도 마찬가지
for _ in range(n):
    x, y = map(int, input().split())
    # 정사각형 가로, 세로 끝 위치 설정
    bx, by = x + 10, y + 10
    for i in range(x, bx):
        for j in range(y, by):
            lst[i-1][j-1] = 1
#print(lst)
# 1인 부분 세기
for k in range(100):
    for l in range(100):
        if lst[k][l] == 1:
            count += 1
print(count)