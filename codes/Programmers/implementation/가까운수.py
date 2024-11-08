# 가까운 수

def solution(array, n):
    answer = 0
    # array 내의 수 정렬
    array = sorted(array)
    # n값이 가장 큰 수면 리스트의 마지막 수가 answer
    if n > array[-1]:
        answer = array[-1]
    else:
        for i in range(len(array)):
            # 같으면 그게 답
            if n == array[i]:
                answer = array[i]
            # n보다 크면 거기서 stop & 비교
            elif n < array[i]:
                # 앞 수와의 차이
                lower = abs(n - array[i-1])
                # 해당 수와의 차이
                upper = abs(n - array[i])
                # 앞 수와의 차이가 해당 수와의 차이보다 작으면 앞 수가 답
                if lower < upper:
                    answer = array[i-1]
                # 앞 수와의 차이가 해당 수와의 차이보다 크면 해당 수가 답
                elif lower > upper:
                    answer = array[i]
                # 앞 수와의 차이와 해당 수와의 차이가 같으면 더 작은 값인 앞 수가 답
                else:
                    answer = array[i-1]
                break
    return answer