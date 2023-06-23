#include <stdio.h>

int main() {
    // num_bas = 바구니 개수, cnt = 시행 횟수
    int num_bas, cnt = 0;
    // start = 시작점, end = 종료점
    int start, end = 0;
    // 첫째줄 받기
    scanf("%d %d", &num_bas, &cnt);
    // bas = 바구니 배열, temp = 임시 배열
    int bas[num_bas];
    int temp[num_bas];
    // 바구니 초기값을 바구니 번호로 초기화
    for (int i = 0; i < num_bas; i++) {
        bas[i] = i + 1;
        temp[i] = i + 1;
    }
    // cnt번 반복
    for (int j = 0; j < cnt; j++){
        // 둘째줄부터 받기
        scanf("%d %d", &start, &end);
        // temp 배열의 인덱스
        int x = start - 1;
        // temp 배열에 5,4,3,2 이런 식으로 역순으로 저장
        for (int k = end; k >= start; k--) {
            x += 1;
            temp[x-1] = bas[k-1];
        }
        // 역순 처리된 temp 배열을 bas 배열 같은 위치에 넣는다.
        for (int m = start; m <= end; m++) {
            bas[m-1] = temp[m-1];
        }
    }
    // bas 배열 하나씩 출력
    for (int n = 0; n < num_bas; n++){
        printf("%d ", bas[n]);
    }
}