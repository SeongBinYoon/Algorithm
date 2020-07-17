//
//  main.c
//  10818
//
//  Created by SeongBinYoon on 2020/03/12.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int n,num;
    int max = -1000001;
    int min = 1000001;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &num);
        if(num > max){
            max = num;
        }
        if(num < min){
            min = num;
        }
        
    }
    printf("%d %d\n", min, max);
    return 0;
}
