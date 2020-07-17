//
//  main.c
//  2446
//
//  Created by SeongBinYoon on 2020/03/17.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    int n;
    scanf("%d",&n);
    for(int i = 0; i < n; i++){
        
        for(int j = 0; j < i; j++){
            printf(" ");
        }
        for(int k = 2 * n - 1 - 2 * i; k > 0; k--){
            printf("*");
        }
        for(int l = 0; l < i + 1; l++){
            printf("");
        }
        printf("\n");
    }
    
    for(int m = 0; m < n - 1; m++){
        
        for(int o = n - 2 - m; o > 0; o--){
            printf(" ");
        }
        for(int p = 0; p < 2 * m + 3; p++){
            printf("*");
        }
        for(int q = n - 2; q > 0; q--){
            printf("");
        }
        printf("\n");
    }
    return 0;
}
