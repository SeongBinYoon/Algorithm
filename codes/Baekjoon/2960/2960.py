# 2960 에라토스테네스의 체

def sieve(n, k):
    # 1. 0~N 모든 정수를 적는다.
    lst = [i for i in range(n+1)]
    cnt = 0
    # 모든 수를 짚어가며 확인
    for i in range(2, n+1):
        # 이미 지워졌으면 다음 수로 넘어간다.
        if lst[i] == 0:
            continue
        # 2. 아직 지우지 않은 수 중 가장 작은 수
        else:
            # 3. 이 수 p부터 p의 배수만큼 지운다. 아직 지우지 않은 p의 배수를 크기 순서대로 지운다.
            for j in range(i, n+1, i): # j는 2~n까지
                # 이미 지워진 수면 다음 수로 넘어간다.
                if lst[j] == 0:
                    continue
                # 지워지지 않은 수면 지우고, 카운트 +!
                else:
                    lst[j] = 0
                    cnt += 1
                    # k와 같으면 해당 수 리턴
                    if k == cnt:
                        return j

n, k = map(int, input().split(' '))
print(sieve(n, k))