//
//  main.c
//  10996
//
//  Created by SeongBinYoon on 2020/03/19.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

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
