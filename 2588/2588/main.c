//
//  main.c
//  multiply
//
//  Created by SeongBinYoon on 2020/03/08.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(){
    
    int a,b;
    scanf("%d %d",&a,&b);
    printf("%d\n", (b%100%10) * a);
    printf("%d\n", (b%100/10) * a);
    printf("%d\n", (b/100) * a);
    printf("%d\n", b * a);
    
    return 0;
}
