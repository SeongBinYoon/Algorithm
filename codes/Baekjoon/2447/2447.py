# 2447 별 찍기-10

def star(n):
    
    # 출력 결과가 3x3 박스라고 가정했을 때, 1,2,3번 가로로 나눈다.
    # for문 x3으로 1,2,3번 줄을 채운다고 생각한다.
    
    # n이 1일 때 '*'출력
    if n == 1:
        return ['*']
    # 재귀 호출로 stars에 담는다.
    stars = star(n//3)
    frame = []

    for s1 in stars:
        frame.append(s1*3)
    for s2 in stars:
        frame.append(s2+' '*(n//3)+ s2)
    for s3 in stars:
        frame.append(s3*3)
    return frame

n = int(input())
print('\n'.join(star(n)))