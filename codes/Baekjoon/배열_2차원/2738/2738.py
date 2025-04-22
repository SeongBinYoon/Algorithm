# 2738 행렬 덧셈
# 지속적인 런타임에러(EOFerror) -> n과 m이 다를 수 있으므로 두번째 for도 m이 아닌 n번 반복

a, b = [], []
n, m = map(int, input().split())

# 행렬 생성
for _ in range(n):
    arow = list(map(int, input().split()))
    a.append(arow)
for _ in range(n):
    brow = list(map(int, input().split()))
    b.append(brow)
#print(a, b)

# 요소 덧셈
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()