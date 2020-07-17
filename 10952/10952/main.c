//
//  main.c
//  10952
//
//  Created by SeongBinYoon on 2020/03/09.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int a,b;

    while(1){
        scanf("%d %d", &a, &b);
        if(a == 0 && b == 0){
            break;
        }
        else
            printf("%d\n", a + b);
       
    }
        
    return 0;
}
