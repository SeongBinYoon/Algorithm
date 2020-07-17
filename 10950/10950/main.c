//
//  main.c
//  a+b-3
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main() {
    // insert code here...
    int N,a,b;
    scanf("%d\n", &N);
    for(int i = 0; i < N; i++){
        scanf("%d %d\n", &a, &b);
        printf("%d\n", a + b);
    }
    

    return 0;
}
