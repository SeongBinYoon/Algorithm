#include <stdio.h>

int main() {
    // num_bas = 바구니 개수, cnt = 시행 횟수
    int num_bas, cnt = 0;
    // start = 시작 바구니, end = 종료 바구니, num_ball = 공 번호
    int start, end, num_ball = 0;
    // 첫째줄 받기
    scanf("%d %d\n", &num_bas, &cnt);
    // bas = 바구니 배열
    int bas[num_bas];
    // 바구니에 초기값 0 초기화
    for (int w = 0; w < num_bas; w++) {
        bas[w] = 0;
    }
    // cnt번 줄에 걸쳐 반복
    for (int i = 0; i < cnt; i++){
        // 둘째줄부터 받기
        scanf("%d %d %d", &start, &end, &num_ball);
        // start부터 end까지 반복하며 bas에 num_ball 집어넣기
        for (int j = start; j <= end; j++)  {
            bas[j-1] = num_ball;
        }
    }
    // bas 배열 하나씩 출력
    for (int k = 1; k <= num_bas; k++){
        printf("%d ", bas[k-1]);
    }
}