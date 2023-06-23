#include <stdio.h>

int main() {
    // num_bas = 바구니 개수, cnt = 시행 횟수
    int num_bas, cnt = 0;
    // c1 = 바꿀 바구니1, c2 = 바꿀 바구니2
    int c1, c2 = 0;
    // 첫째줄 받기
    scanf("%d %d\n", &num_bas, &cnt);
    // bas = 바구니 배열
    int bas[num_bas];
    // 바구니 초기값을 바구니 번호로 초기화
    for (int w = 0; w < num_bas; w++) {
        bas[w] = w + 1;
    }
    // cnt번 줄에 걸쳐 반복
    for (int i = 0; i < cnt; i++){
        // 둘째줄부터 받기
        scanf("%d %d", &c1, &c2);
        // c1과 c2를 교환
        int temp = bas[c1-1];
        bas[c1-1] = bas[c2-1];
        bas[c2-1] = temp;
    }
    // bas 배열 하나씩 출력
    for (int k = 1; k <= num_bas; k++){
        printf("%d ", bas[k-1]);
    }
}