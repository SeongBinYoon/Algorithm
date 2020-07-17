//
//  main.c
//  11021
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    int a,b;
    scanf("%d",&T);
    for(int i = 0; i < T; i++){
        scanf("%d %d", &a, &b);
        printf("\n%s%d%s%d\n", "Case #", i + 1,": ", a + b);
    }
    return 0;
}
