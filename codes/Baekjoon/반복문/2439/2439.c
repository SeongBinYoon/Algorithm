// 2439 별찍기 - 2

#include <stdio.h>

int main() {
    // insert code here...
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        for(int j = N - i - 1; j >= 1; j--){
            printf(" ");
        }
        
        for(int k = 1; k < i + 2; k++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
