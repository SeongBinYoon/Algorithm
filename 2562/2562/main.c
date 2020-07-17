//
//  main.c
//  2562
//
//  Created by SeongBinYoon on 2020/03/15.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int n;
    int max = 0;
    int cnt = 0;
    for(int i = 0; i < 9; i++){
        scanf("%d",&n);
        if(n > max){
            max = n;
            cnt += 1;
        }
        
    }
    printf("%d\n", max);
    printf("%d\n", cnt);
    return 0;
}
