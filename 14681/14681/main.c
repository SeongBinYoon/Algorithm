//
//  main.c
//  14681
//
//  Created by SeongBinYoon on 2020/03/16.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int x,y;
    scanf("%d\n%d",&x,&y);
    
    if(x > 0 && y > 0){
        printf("1\n");
    }
    else if(x < 0 && y > 0){
        printf("2\n");
    }
    else if(x < 0 && y < 0){
        printf("3\n");
    }
    else if(x > 0 && y < 0){
        printf("4\n");
    }
    return 0;
}
