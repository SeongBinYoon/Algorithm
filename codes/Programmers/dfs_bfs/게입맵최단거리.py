# 게임 맵 최단거리
# 최단거리 - bfs 유리
from collections import deque

def solution(maps):
    answer = 0
    # 상하좌우
    dx = [-1, 1, 0, 0]  # 행(상, 하)
    dy = [0, 0, -1, 1]  # 열(좌, 우)
    
    # bfs
    def bfs(x, y):
        # queue 생성
        queue = deque()
        # queue에 현재 위치 (x, y) 튜플 삽입
        queue.append((x, y))
        # queue에 아무것도 없을 때까지 반복
        while queue:
            # 선입선출로 x, y 꺼냄
            x, y = queue.popleft()
            
            # 상하좌우 확인 (x, y는 현재 위치, nx, ny는 앞으로 움직일 위치)
            for i in range(4):
                nx = x + dx[i]  # 행
                ny = y + dy[i]  # 열
            
                # 경계를 넘어가면 반복문 다시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                # 벽이어도 반복문 다시
                if maps[nx][ny] == 0:
                    continue
                # 방문하지 않은 길이면 해당 위치에 +1
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    # queue에 삽입
                    queue.append((nx, ny))
        # queue가 비워지면 마지막 칸 리턴
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    
    # 마지막이 막혀있으면 answer = 1이 됨. 그럼 -1 리턴
    if answer == 1:
        return -1
    else:
        return answer

