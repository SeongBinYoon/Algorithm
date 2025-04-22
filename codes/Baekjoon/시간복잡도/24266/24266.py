# 24266 알고리즘 수업-알고리즘의 수행시간5

# 수행횟수는 n^3 이며, 최고차항의 차수는 O(n^3)이므로 3이다.
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''
n = int(input())
print(n**3)
print(3)