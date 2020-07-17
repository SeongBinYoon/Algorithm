//
//  main.c
//  2523
//
//  Created by SeongBinYoon on 2020/03/15.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main() {
    
    int n;
    scanf("%d",&n);
    for(int i = 0; i < n; i++){
        for(int j = 1; j < i + 2; j++){
            printf("*");
        }
        for(int k = n - i - 1; k >= 1; k--){
            printf(""); //스페이스를 넣으면 출력초과됨. 한칸공백이 아니라 Null을 넣을 것.
        }
        printf("\n");
    }
    
    for(int l = 0; l < n; l++){
        for(int m = n - l; m > 1; m--){
            printf("*");
        }
        for(int p = 0; p < n + l; p++){
            printf(""); //위와 마찬가지.
        }
        printf("\n");
    }
    
    return 0;
}
