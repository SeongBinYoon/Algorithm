# 겹치는 선분의 길이

def solution(lines):
    answer = 0
    # 전체 값 임시 리스트
    tmp = []
    # 범위의 최소, 최대를 알기 위함
    for i in range(3):
        for j in range(2):
            tmp.append(lines[i][j])
    upper = max(tmp)
    lower = min(tmp)
    # 방문 리스트 (0~1, 1~2..구간을 나타냄)
    visited = [0 for _ in range(upper-lower)]
    # 구간 변경을 위한 값
    target = -lower
    # 구간 0~ 로 변경
    for i in range(3):
        for j in range(2):
            lines[i][j] = lines[i][j] + target
    # 각 구간 a,b에 대하여
    for k in range(3):
        a, b = lines[k]
        # 해당하는 인덱스 +1씩 방문 처리
        for l in range(a, b, 1):
            visited[l] += 1
    # visited 확인하며 2 이상이면 겹치는 부분
    for s in range(len(visited)):
        if visited[s] > 1:
            answer += 1
    return answer