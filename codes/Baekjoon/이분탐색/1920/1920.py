# 1920 수 찾기

def solution(nset, mlst):
    for i in range(len(mlst)):
        if mlst[i] in nset:
            print(1)
        else:
            print(0)

n = int(input())
nset = set(map(int, input().split(' ')))
m = int(input())
mlst = list(map(int, input().split(' ')))
solution(nset, mlst)