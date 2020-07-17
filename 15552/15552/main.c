//
//  main.c
//  15552
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main() {
    // insert code here...
    int T;
    int a,b;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%d %d", &a, &b);
        printf("%d", a+b);
    }
    return 0;
}
