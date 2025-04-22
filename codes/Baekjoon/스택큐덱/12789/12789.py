# 12789 도키도키 간식드리미

# 한 명씩 들어갈 수 있는 공간/간식 받는 줄/현재 학생 대기줄
space, line, stand = [], [], []
n = int(input())
stand = list(map(int, input().split(' ')))      # 5, 4, 1, 3, 2
# 정답
answer = sorted(stand)                          # 1, 2, 3, 4, 5

# 원하는 수 카운팅
num = 1
# phase1: 대기 줄 비우기
while stand != []:
    # 맨 앞 수가 num과 같으면
    if stand[0] == num:
        line.append(stand[0])               # 맨 앞 수 바로 line에 추가
        num += 1                            # num 최신화
        stand = stand[1:]                   # 대기줄 최신화
    # 맨 앞 수가 num과 다르면 이번엔 space와 비교
    else:
        # space가 비어있을 때
        if space == []:
            space.append(stand[0])          # 맨 앞 수 바로 space에 추가
            stand = stand[1:]               # 대기줄 최신화
        # space에 뭐라도 들어있을 때
        else:
            if space[-1] == num:            # space의 끝 수가 num과 같으면
                line.append(space[-1])      # space의 끝 수 line에 추가
                num += 1                    # num 최신화
                space.pop()                 # space 최신화
            else:                           # space의 끝 수가 num과 다르면
                space.append(stand[0])      # 맨 앞 수 space에 추가
                stand = stand[1:]           # 대기줄 최신화
    # print(line, space, stand)
# print(line, space, stand)

# phase2: 1인이 들어가는 공간 비우기
while space != []:
    line.append(space[-1])
    space.pop()

# 정답과 비교
if line == answer:
    print("Nice")
else:
    print("Sad")