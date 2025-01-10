# 11729 하노이의 탑 이동 순서

# 하노이의 탑
# 1. 한번에 한 개의 원판만을 다른 탑으로 옮길 수 있음
# 2. 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

# 하노이의 탑 재귀 알고리즘
# 1. <재귀> 출발말뚝 상위 n-1개의 원반을 임시말뚝으로 옮김
# 2. 출발말뚝의 맨 아래에 남아 있는 가장 큰 원반을 도착말뚝으로 옮김
# 3. <재귀> 임시말뚝의 원반 n-1개를 도착말뚝으로 옮김

def tower_of_hanoi(n, source, dest, temp):
    global count        # 전역 변수
    if n > 1:
        # n=3인 경우, 먼저 2개의 원반을 source->temp로 옮김
        tower_of_hanoi(n-1, source, temp, dest)
        # 가장 아래의 큰 원반 1개를 source->dest로 옮김
        count += 1
        lst.append([source, dest])
        # temp에 옮겨놨던 2개의 원반을 temp->dest로 옮김
        tower_of_hanoi(n-1, temp, dest, source)
    else:
        # 원반이 1개 남은 경우 dest로 옮김
        count += 1
        lst.append([source, dest])

n = int(input())
count = 0
lst = []
tower_of_hanoi(n, '1', '3', '2')
print(count)
for i in range(len(lst)):
    for j in range(2):
        print(lst[i][j], end=' ')
    print()