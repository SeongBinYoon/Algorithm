//
//  main.c
//  compare
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main() {
    // insert code here...
    int a,b;
    scanf("%d %d", &a, &b);
    if(a > b){
        printf(">\n");
    }
    else if(a < b){
        printf("<\n");
    }
    else
        printf("==\n");
    
    return 0;
}
