# 14889 스타트와 링크

import sys
input = sys.stdin.readline

# 행렬 리스트, 최솟값 결과 변수
lst = []
minval = sys.maxsize

# 입력
n = int(input())
for i in range(n):
    lst.append(list(map(int, input().split())))

# 방문 리스트
visited = [0] * n

# Backtracking + DFS
# cnt=지금까지 선택된 사람 수, idx=앞으로 선택될 사람 인덱스
def startlink(cnt, idx):
    global minval
    # 탐색 종료 조건 = 노드 절반 돌면 나머지는 정해짐
    if cnt == n // 2:
        # start, link 팀 능력치 초기화
        start, link = 0, 0
        # 행 및 열 돌며 능력치 연산
        for i in range(n):
            for j in range(n):
                # i, j 둘다 방문했다면(i+1번과 j+1번 사람은 같은 팀)
                if visited[i] and visited[j]:
                    start += lst[i][j]
                # i, j 둘다 방문하지 않았다면(i+1번과 j+1번 사람은 같은 팀)
                elif not visited[i] and not visited[j]:
                    link += lst[i][j]
                # 방문을 안한 곳이 하나라도 있다면(visited에 하나라도 0이면) 넘김
        minval = min(minval, abs(start - link))
        return
    
    # 탐색 종료 전(지금까지 선택된 인덱스 제외, 선택되지 않은 남은 사람 인덱스 돌기)
    for k in range(idx, n):
        # 방문하지 않았다면 방문
        if visited[k] == 0:
            visited[k] = 1
            # 다음 사람 선택
            startlink(cnt+1, k+1)
            visited[k] = 0

startlink(0, 0)
print(minval)