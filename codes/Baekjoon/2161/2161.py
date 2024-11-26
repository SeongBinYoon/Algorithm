# 2161 카드1

n = int(input())
lst = [i for i in range(1, n+1)]
dump = []
for _ in range(n-1):
    # 제일 위 카드를 버린다.
    dump.append(lst[0])
    # 다음 카드를 제일 아래로(뒤로) 옮긴다.
    lst.append(lst[1])
    # lst 최신화
    lst = lst[2:]

# 마지막 남은 카드도 합쳐서 출력
dump.append(lst[0])
for s in dump:
    print(s, end=' ')