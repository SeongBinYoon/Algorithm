# 24264 알고리즘 수업 - 알고리즘의 수행 시간3

# 이중 for 반복문을 통해 n*n번만큼 시행한다. 또한 최고차항의 차수는 항상 2(제곱)이다.
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

n = int(input())
print(n**2)
print(2)