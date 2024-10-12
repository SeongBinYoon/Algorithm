# 10250 ACM 호텔

t = int(input())
# 우선순위대로 방 카운트
cnt = 0
# 방 번호
room = 0
for _ in range(t):
    h, w, n = map(int, input().split())
    for i in range(w):
        for j in range(h):
            cnt += 1
            if cnt == n:
                room = (j+1) * 100 + (i+1)
    print(room)
    cnt = 0