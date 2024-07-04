// 10996 별찍기 - 21 -> 수정 필요

#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            for(int j = 0; j < 1; j++){
                printf("*");
            }
            for(int k = 0; k < 1; k++){
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}
