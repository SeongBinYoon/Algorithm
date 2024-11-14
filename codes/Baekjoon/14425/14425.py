# 14425 문자열 집합

def solution(nlst, mlst):
    cnt = 0
    for i in range(len(mlst)):
        if mlst[i] in nlst:
            cnt += 1
    return cnt

nlst = []
mlst = []
N, M = map(int, input().split(' '))
for _ in range(N):
    nlst.append(input())
for _ in range(M):
    mlst.append(input())

print(solution(nlst, mlst))