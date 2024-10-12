# 10768 특별한 날

m = int(input())
d = int(input())

# 2월 18일 전인 경우
if (m < 2) or (m == 2 and d < 18):
    print("Before")
# 2월 18일인 경우
elif m == 2 and d == 18:
    print("Special")
# 2월 18일 후인 경우
else:
    print("After")