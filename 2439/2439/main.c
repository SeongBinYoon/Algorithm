//
//  main.c
//  2439
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

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
