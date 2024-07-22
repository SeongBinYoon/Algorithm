# 2920 음계

# 입력 받기
note = input().split()
mixflag = 0
# 각 음계 int형으로 변환
for i in range(len(note)):
    note[i] = int(note[i])

# 하나씩 돌며 확인
# ascending
if note[1] - note[0] == 1:
    for j in range(len(note)-1):
        # 도중에 한번이라도 끊기면 mixed 출력 후 반복문 종료
        if note[j+1] - note[j] != 1:
            print("mixed")
            mixflag = 1
            break
    if mixflag == 0:
        print("ascending")
# descending
elif note[1] - note[0] == -1:
    for k in range(len(note)-1):
        # 도중에 한번이라도 끊기면 mixed 출력 후 반복문 종료
        if note[k+1] - note[k] != -1:
            print("mixed")
            mixflag = 1
            break
    if mixflag == 0:
        print("descending")
# mixed
else:
    print("mixed")