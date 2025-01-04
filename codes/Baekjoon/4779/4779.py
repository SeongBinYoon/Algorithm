# 4779 칸토어 집합

def solution(n):
    # 길이가 1이면 그대로 출력
    if n == 1:
        return "-"
    # 길이가 2이상이면 다음 수행
    else:
        # 전반부 파라미터로 넘겨 재귀
        leftorright = solution(n // 3)
        # 중간부 공백
        center = " " * (n // 3)
        # 중간부를 중심으로 좌우는 대칭이므로 합침
        return leftorright + center + leftorright
# 입력
while True:
    try:
        N = int(input())
        print(solution(3 ** N))
    except:
        break