//
//  main.c
//  three integers
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int a,b,c;
    scanf("%d %d %d", &a,&b,&c);
    if(a <= b && b <= c){
        printf("%d\n", b);
    }
    else if(a <= c && c <= b){
        printf("%d\n", c);
    }
    else if(a >= b && a <= c){
        printf("%d\n", a);
    }
    else if(c <= a && a <= b){
        printf("%d\n", a);
    }
    else if(b <= c && c <= a){
        printf("%d\n", c);
    }
    else if(c <= b && b <= a){
        printf("%d\n", b);
    }
    return 0;
}
