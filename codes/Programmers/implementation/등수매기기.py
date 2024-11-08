# 등수 매기기

def solution(score):
    answer = []
    tmp = []
    # 리스트 길이만큼 돌며 내부 리스트 확인
    for i in range(len(score)):
        # 내부 리스트 값 더하고 2로 나눠 평균을 구함 -> 몫이 아닌 나누기를 해야 함
        average = sum(score[i]) / 2
        # 임시 리스트에 평균 삽입
        tmp.append(average)
    # 역정렬한 리스트에서 tmp의 요소의 위치+1 한 것이 순위가 됨
    answer = [sorted(tmp, reverse=True).index(s)+1 for s in tmp]
    return answer