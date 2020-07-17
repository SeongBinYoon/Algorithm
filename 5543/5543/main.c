//
//  main.c
//  hamburger
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int a,b,c,d,e;
    int h = 0;
    int dr = 0;
    scanf("%d %d %d %d %d", &a,&b,&c,&d,&e);
    if(a <= b && a <= c){
        h = a;
    }
    else if(b <= a && b <= c){
        h = b;
    }
    else if(c <= a && c <= b){
        h = c;
    }
    if(d <= e){
        dr = d;
    }
    else if(e <= d){
        dr = e;
    }
    printf("%d\n", h + dr - 50);
    
    return 0;
}
