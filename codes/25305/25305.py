# 25305 커트라인

n, k = map(int, input().split())
lst = input().split()
# 문자형 -> 정수형
for i in range(n):
    lst[i] = int(lst[i])

# bubble sort
for i in range(0, n-1):
    for j in range(0, n-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst[-k])