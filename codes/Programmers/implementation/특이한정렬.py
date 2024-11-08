# 특이한 정렬

def solution(numlist, n):
    answer = []
    # n과 요소의 차를 담는 리스트
    diff = []
    # 차이가 같은 경우 더 큰 수를 먼저 정렬하므로 index() 사용을 위해 역정렬
    numlist = sorted(numlist, reverse=True)
    # 요소를 돌아가면서 차이를 diff에 담는다.
    for s in numlist:
        diff.append(abs(n-s))
    # numlist가 빌 때까지 반복
    while numlist != []:
        # 차이 중 최소값의 인덱스 저장
        idx = diff.index(min(diff))
        # 해당하는 값을 리스트에 저장
        answer.append(numlist[idx])
        # numlist와 diff 각각 해당 값은 제거
        numlist = numlist[:idx] + numlist[idx+1:]
        diff = diff[:idx] + diff[idx+1:]
    return answer