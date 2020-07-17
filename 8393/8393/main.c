//
//  main.c
//  8393
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int n;
    int arr = 0;
    int sum = 0;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        arr = i;
        sum = sum + arr;
    }
    printf("%d\n",sum);
    return 0;
}
